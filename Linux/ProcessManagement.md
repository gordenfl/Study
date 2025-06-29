# Process Management

0. Attribute In Process
    每一个进程都在内核有一个结构体:task_struct来保存. 这个结构体非常复杂, 这里列一些说明:
    进程的meta信息: pid,tgid(线程组ID), comm(进程名), state(如:睡眠,运行,就绪等), flags(各种标志位)
    内存管理信息: mem_struct * mm(当前进程的用户态的空间),  active_mm(内核线程用来共享其他的线程), vm_area_struct(链表或树,来描述虚拟内存区域), page_table_mapping(页表指针,就是虚拟地址与物理地址的映射)
    进程调度信息: prio/static_prio (当前优先级), sched_class(调度类型,一本就是CFS), rt_priority(实时进程的优先级), se(shed_entity,用于公平调度的权重结构), CPU(运行在哪个CPU上)
    文件系统信息: fs_struct *fs(进程的文件系统视图,包括目录, 根目录), files_struct *file (文件描述符表, fd->打开的文件), file *fd[](指向已经打开的文件指针,可以通过 open, read 等系统调用访问)
    信号处理: sighand_struct *sighand (这个是信号处理的函数表), sigpending(挂起信号的集合), blocked(被阻塞的信号集合), signal_struct *signal (与线程组共享的信号状态)
    进程间关系的信息: real_parent(实际的父进程), parent(当前父进程, 这个可能会被ptrace该表TODO), children(子进程链表), sibling(兄弟进程链表), group_leader(线程组组长)
    线程和信号量相关的信息: thread_info(存放在内核栈地步的简化信息), stack(内核栈指针),sem(用于信号量操作的数据结构)
    资源使用与限额信息: rlim[](资源限制,比如最大文件数,最大栈空间), utime/stime (用户态/内核态使用的CPU时间), start_time(启动的时间), cputime_exires(计时器)
    命名空间与安全信息: nsproxy(包括UTS, IPC, PID, mount等命名空间指针), cred(进程的安全凭证,比如:UID< GID, capabilities)

    你可以通过一些途径去查看进程的这些年描述信息: 
    - 查看/proc/[pid]/ 里面的东西,就可以看到这个进程的一些信息,比如status, maps, fds/ 等等

1. Process creation
    fork(): copy the father process to create a new process
    vfork(): like fork, but all the process of father and child share the memory, until the exec()
    clone(): TODO: it's more base layer
    exec(): replace the executable code to another program let this process. all the code segement are replace to new execute code

    举例:当用户调用fork后, 系统通常会通过一下步骤去实现新进程创建

    ```txt
    从上到下按次序执行:
    User Space : 下面执行是在用户态
      fork()
      sys_fork()或者 do_fork()
    Kernel Space: 下面执行在内核态
      kernel_clone()/do_fork()
      copy_process(): 
      create new task_struct
      setup the resource include: Memory, Fd, signal deal, schedule info
      add the sub process into the scheduling system
      return pid(to father) And ppid (to child) to processes.
    ```
    
    ```
    fork()如果调用成功以后,父进程会得到子进程的pid, 子进程会得到0, 如果失败就是负数.子进程会复制父进程所有的内容
    fork()->sys_fork()/do_fork() 这是一个用户态的系统调用,会让这个执行过程陷入内核态状态,去执行内核的do_fork()/kernel_clone()
    ------下面全部都是内核态的工作了---------
    内核态中的do_fork(clone_flags, stack_start ...)这个函数是Linux创建进程的唯一接口, 他会按照不同的参数做不同的事情,比如创建线程,创建进程等等,都会在这里执行.这个函数会调用一个叫做 copy_process的函数就是核心的复制逻辑, 他会做:
    a. 创建子进程的task_struct, 包含进程核心数据结构用来保存pid, 状态, 调度信息,父子关心就是[0. Attribute In Process]中描述的核心数据, 并会通过 dup_task_struct() 分配并初始化子进程的task_struct
    b. 拷贝资源: 使用copy_mm() 拷贝或者共享内存描述符, copy_files()文件描述符表,copy_sighand() 信号处理, copy_sched()复制实体
    c. 设置PID,和链接父子关系
    d. 把进程加入到就绪队列,准备被调度 使用的是: wake_up_new_task()
    ```

2. Process Scheduling
    这个部分就是调度进程如何执行,因为进程很多CPU就几个, 如何分配这些进程在什么时间到什么CPU上执行就成为一个非常重要的任务,这部分就是做这个事情的.
    他有一个平衡因素表:
    包括的属性有
    * ⏱ 响应时间（对交互式程序快）
    * 💪 吞吐量（每秒完成的任务数）
    * ⚖️ 公平性（所有进程都有机会）
    * 🧠 优先级控制（关键任务优先）

    具体详细结构我这里不说,我直说原理, 调度的时候他并不是随时进行调度的,而是通过时钟中断形式或其他事件发生的时候进行调度.我列一下:
    * 时钟中断 (周期性触发, 一般是每隔几毫秒一次)
    * 进程主动放弃CPU (比如进程调用了sleep, sched_yield或者IO阻塞)
    * 进程被抢占 因为进程描述信息中有优先级,当优先级高的进程被启动,这个时候就会占用优先级低的进程所使用的CPU等资源
    * 中断,或者系统调用返回: 某些系统调用会触发进程调度

3. Process Terminal
    进程终结的方式有几种:

| 方式                | 描述                            |
| ----------------- | ----------------------------- |
| 正常退出              | 程序执行完 `main()` 函数或调用 `exit()` |
| 异常终止              | 错误或断言失败，如段错误（SIGSEGV）         |
| 调用 `exit_group()` | 多线程程序中终止整个线程组                 |
| 被其他进程杀死           | 例如收到 `SIGKILL`、`SIGTERM`      |
| 父进程调用 `kill()`    | 向子进程发送信号                      |
| 用户使用 `Ctrl+C`     | 向前台进程组发送 `SIGINT`             |

当进程进入到终结的流程之后他的流程会是:
```
exit() / _exit()   这是在用户态执行的下面所有的都是在核心态执行
   ↓
do_exit() 释放文件描述符, 虚拟内存空间释放, 信号处理(给他的父进程发消息SIGCHLD), PID表清理置为ZOMBIE 等等.
   ↓
release resources (files, memory, etc.)
   ↓
exit_notify() → 通知父进程，发送 SIGCHLD
   ↓
设置状态为 ZOMBIE（僵尸）
   ↓
父进程调用 wait()
   ↓
do_wait()
   ↓
release_task() → 真正销毁 task_struct
```

4. Context Switch
    Linux 支持多种调度策略 policies:
    * SCHED_NORMAL: 普通进程调策略, 会使用红黑树 CFS(完全公平调度器)实现,绝大多数process都会被这种调度
    * SCHED_BATCH: 批处理调度策略, 他的调度类似CFS但是没有那么多的交互性,在batch中间就不会有交互
    * SCHED_IDLE: 优先级调度策略, 就是最低优先级的进程只会在系统空闲的时候才调y'y
    * SCHED_FIFO: 实时级调度策略, 先来先服务,直到主动让出CPU
    * SCHED_RR: 实时轮转, 实时任务使用时间片轮换调度

    可用这个命令看调度策略
    ```shell
    chrt -p 1234  # 查看 PID 为 1234 的进程调度策略
    ```
    每一个进程可以选择自己的调度策略,在运行过程中也可以改变调度策略.

    
5. Process Status

| 状态代号 | 状态名称                     | 含义简述                    |   查看           |
| ---- | ------------------------ | ----------------------- |--------------|
| R    | Running / Runnable       | 正在 CPU 上运行，或可运行（就绪）     | ps -eo pid,stat,comm \| grep ' R'  |
| S    | Sleeping (interruptible) | 可中断睡眠，等待某事件（如 I/O）      | ps -eo pid,stat,comm \| grep ' S'  |
| D    | Uninterruptible sleep    | 不可中断睡眠，常用于等待硬件响应        | ps -eo pid,stat,comm \| grep ' D'  |
| Z    | Zombie                   | 僵尸状态，进程已退出但未被父进程回收      | ps -eo pid,stat,comm \| grep ' Z'  |
| T/t  | Stopped / Traced         | 停止执行（如收到 `SIGSTOP`）或被调试 | ps -eo pid,stat,comm \| grep ' T'  |
| X    | Dead（很少见）                | 进程已终止，正在被清理（瞬间状态）       | ps -eo pid,stat,comm \| grep ' X'  |

X 为什么很少见,因为一般系统回收资源相当快,非常快就消失了,所以就没有可能看到X
另外你可以通过```/proc/[pid]/status``` 来查看 

```text
               创建进程
                   ↓
               [ R ]  ←─ 被调度运行
             ↙   ↑  ↘
        [ S ]   ↑   [ T ]
      睡眠等待  ↑   被暂停/调试
             ↘ ↓ ↙
              [ D ] ← 不可中断等待
                   ↓
               [ Z ] ← 执行结束 → 等待父进程回收
                   ↓
                 销毁（资源释放）

```

进程的状态变表

6. CFS - Completely Fair Scheduler
    CFS调度的流程:
    CFS是默认调度器(Completely Fair Scheduler)完全公平调度器, 他的实现是一棵红黑树.每个进程都有vruntime(执行时间), 这个数值越小就说明这个进程很少用到CPU, 就优先会被调度到.如果当前进程不在最公平的时候,就会触发CFS调度.

    进程调度的流程大概是:
    * 保存当前进程的寄存器,堆栈指针,等上下文
    * 更新当前CPU的current 指针为下一个进程
    * 回复新的进程的寄存器,堆栈, 页表等信息
    * 切换完成,继续运行新进程

    核心函数:

    ```c
    context_switch(prev, next);
    ```




[Back to Index](./Basic%20Constructure%20of%20Linux.md)