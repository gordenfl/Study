# Inner SpinLock

SpinLock 就是用了X86中的原子操作 test_and_set 和 xchg 这两种指令,完成对锁的变量进行修改,确保中间不会被打断.

xchg指令可以将寄存器的值与内存中的数据交换,从而实现锁的获取和释放. 原理如下:

* 如果锁变量原本为 0（未锁定），则 EAX 被设置为 0，锁变量被设置为 1，表示当前线程成功获取锁。
* 如果锁变量原本为 1（已锁定），则 EAX 被设置为 1，表示当前线程未能获取锁，需要继续自旋.

```asm
locked:  ; 锁变量，1 表示锁定，0 表示未锁定
    dd 0

spin_lock:
    mov eax, 1        ; 将 1 加载到 EAX 寄存器
    xchg eax, [locked] ; 原子地交换 EAX 和锁变量
    test eax, eax      ; 测试 EAX 寄存器的值
    jnz spin_lock      ; 如果 EAX 不为 0，表示锁已被占用，继续自旋
    ret                ; 获取锁成功，返回

spin_unlock:
    xor eax, eax       ; 将 EAX 寄存器清零
    xchg eax, [locked] ; 原子地交换 EAX 和锁变量
    ret                ; 释放锁，返回
```

Test and Set 工作原理:

* 读取：获取指定内存位置的当前值。
* 设置：将该内存位置的值设置为 1。
* 返回：返回该内存位置原先的值。

硬件支持, test 和 set 之间不会中断
