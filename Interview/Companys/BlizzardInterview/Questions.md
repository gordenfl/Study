# Blizzard first interview Questions

## Data Structure

1. HashMap : 判断一个字符串是否有重复(存在), unordered_set来做就最高效,O(1), 但是, 底层是hash表实现,set底层是红黑树,如果要判断是否妇女在set是O(lgn), unordered_set 是O(1)(average, the worst is O(n)). 优先使用unordered_xxx 查找插入更快, 适合在只关心是否存在的场景.

2. Stack and Queue
 
3. LinkedList

4. Binary Tree

5. Sort Alg: Quick Sort (一般情况O(nlgn), 最坏情况O(n^2))

| 排序算法     | 最好时间                 | 最坏时间       | 平均时间       | 空间复杂度          | 稳定性   | 备注               |
| -------- | -------------------- | ---------- | ---------- | -------------- | ----- | ---------------- |
| **冒泡排序** | O(n)                 | O(n²)      | O(n²)      | O(1)           | ✅ 稳定  | 简单，适合教学          |
| **选择排序** | O(n²)                | O(n²)      | O(n²)      | O(1)           | ❌ 不稳定 | 总是查找最小           |
| **插入排序** | O(n)                 | O(n²)      | O(n²)      | O(1)           | ✅ 稳定  | 小规模数据效率高         |
| **希尔排序** | O(n log n)\~O(n^1.3) | O(n²)      | 依赖步长序列     | O(1)           | ❌ 不稳定 | 插入排序的改进版         |
| **归并排序** | O(n log n)           | O(n log n) | O(n log n) | O(n)           | ✅ 稳定  | 分治法              |
| **快速排序** | O(n log n)           | O(n²)      | O(n log n) | O(log n)\~O(n) | ❌ 不稳定 | 平均非常快            |
| **堆排序**  | O(n log n)           | O(n log n) | O(n log n) | O(1)           | ❌ 不稳定 | 使用堆结构            |
| **计数排序** | O(n + k)             | O(n + k)   | O(n + k)   | O(n + k)       | ✅ 稳定  | 适用于整数、小范围        |
| **桶排序**  | O(n + k)             | O(n²)      | O(n + k)   | O(n + k)       | ✅ 稳定  | 依赖分布均匀           |
| **基数排序** | O(n·k)               | O(n·k)     | O(n·k)     | O(n + k)       | ✅ 稳定  | k为位数，适用于定长整数或字符串 |


## Algorithm

1. Dynamic Program

2. Sliding Window

3. String Deal

## C++ and memory

1. Pointer and Reference: 
    * Pointer: 根据申明来确定他是在堆还是栈, new 的就在堆, 直接申明的就是在栈上
        * pointer is a variable store the address of another variable. you can modify the variable value from it.
        * pointer can be nullptr does not point to any address
        * pointer can be assign value let pointer another variable
        * pointer can be make calc, such like add+ sub-, etc.
        * pointer can have multi-level, such like int **

    * Reference: 没有内存占用,只是编译时展开而已
        * Reference must be initialed while declaration ```int &a = xxx;```. you could not ```int &a;```
        * Reference can not be NULL or nullptr; it should bind to another variable
        * Reference could not bind another variable

2. Deep copy and Shallow copy
    * Shallow copy: 浅拷贝, 这只是让新旧对象指向同一块空间, 只是指针复制,指针指向的内容不会复制.编译器生成的默认拷贝构造函数/复制运算符只会浅拷贝
    * Deep Copy: 深拷贝, 复制对象的时候需要为所有资源飞配独立的新内存,并且复制其内容,新旧对象互不干扰,只是值相同而已.需要手动编写拷贝构造函数.

    * 本身如果类中没有new 出来的东西,直接使用浅拷贝就可以了,不会出问题,如果对象中有new出来的东西,必须写拷贝构造函数,这样不会出问题.

    * std::unique_ptr/std::shared_ptr 来自动管理资源

3. Memory Manage
    * 分为堆(heap)和栈(stack).
    stack: 存放临时变量,函数参数,自动会分配和回收, 速度快, 空间有限通常就几 MB.
    heap: 用于动态分配内存,通过new/malloc, 灵活但需要手动释放,内存泄漏会有大问题, 速度相对较慢

    * RAII与标准库容器: RAII(Resource Acquisition is Initialization), 通过对象生命周期自动管理资源,构造时获取资源,析构时释放资源,标准容器类似vector, map, set string都是这样.

    * 智能指针:std::unique_ptr/std::shared_ptr 自动管理资源, unique_ptr 独占所有权,不能复制.
    shared_ptr 支持引用计数共享所有权,最后一个shared_ptr计数器为0 的时候销毁,释放资源
    weak_ptr: 避免循环引用
    指针的管理方面需要注意的是: 泄露, 悬挂, 双重释放等问题

    * 手动内存管理
    只有在必要的时候,才自己管理内存.比如: 性能临界代码, 需要内存池, 自定义对齐策略.
    delete/new, delete[]/new[] 对齐使用
    malloc/free对齐使用

4. malloc vs new, free vs delete
    * 构造函数调用和不调用,析构函数调用和不调用
    * 返回值: 返回具体类型和void*
    * 异常情况,new抛出异常, malloc return NULL

5. 智能指针 std::shared_ptr, std::unique_ptr, std::weak_ptr
    * unique_ptr:独占指针,只有一个所有制,不能复制(拷贝构造, 和拷贝复制被删除), 智能移动 通过std::move,转移所有权
    * shared_ptr: 共享指针, 可以被多个实例共享所有权.通过内部的引用计数控制资源的声明周期,最后一个share_ptr 析构的时候才释放资源.
    * unique_ptr只存储一个指针,没有额外开销, 速度快,内存占用小
    * shared_ptr: 存储两个指针, 一个是资源指针, 一个是控制块指针, 内部还有一个引用计数,可能参与原子操作和额外分配.
    * unique_ptr 自动析构,无需delete, shared_ptr最后一个引用消失的时候才析构,不过要警惕循环引用,需要配合weak_ptr解决.
    下面的代码会出现循环引用

        ```C++
        class B;  // 前向声明
        class A {
        public:
            std::shared_ptr<B> b_ptr;  // A 拥有 B
            ~A() { std::cout << "A destroyed\n"; }
        };

        class B {
        public:
            std::shared_ptr<A> a_ptr;  // B 拥有 A —— 导致循环引用
            ~B() { std::cout << "B destroyed\n"; }
        };
        ```

        上面的std::shared_ptr< B > b_ptr;  改成std::weak_ptr< B > b_ptr; 就可以避免循环引用

    * weak_ptr: 是一个弱引用的指针可以通过lock来生成shared_ptr, 这样可以判断这个指针是否还存在,如果存在就可以用,如果不存在就去另外的逻辑.

## C++ Features

1. C++ Polymorphism(多态性) implement virtual implement
    * 就是通过一个虚表来让多个子类具有不同的成员函数,调用的时候都会通过这个虚表来定位具体的函数是基类的还是子类的.
    * vtable 的位置是通过在构造的时候产生,他在内部的最后位置有一个vptr,这个vptr就是指向虚表的指针.
    * 每次调用虚函数的时候就会通过这个vptr查询到虚表中的具体函数指针去调用它.
    * 单继承的时候只会有一个vptr, 多继承的时候会有多个vptr, 每个vptr指向对应的基类中virutal函数的列表.

2. abstract virtual class and interface, virtual function
    * interface: 在C++中没有这个关键字,但是可以表示这个函数只有存虚函数,没有任何变量和非纯虚函数的类
    * abstract virtual: 抽象类必须有纯虚函数,可以有非纯虚函数,和变量定义
    * virtual function: 就是在C++多台中的函数定义,可以被子类重写,子类对象调用的时候,只会调用子类的实现,基类的实现只会在没有实现这个虚函数的时候被调用.

3. 虚拟继承 virtual public

    ```CPP
    class A { /*...*/ };
    class B : public A { /*...*/ };
    class C : public A { /*...*/ };
    class D : public B, public C { /*...*/ };
    ```

    这样D里面会有两个A, 可能导致成员变量重复, 如果```D d;``` 然后调用这个 ``` d.foo(); ``` foo是在A中实现的, 这就麻烦了,所以需要有虚拟继承:

    ```CPP
    class A { /*...*/ };
    class B : virtual public A { /*...*/ };
    class C : virtual public A { /*...*/ };
    class D : public B, public C { /*...*/ };
    ```

    D中只包含一个A的子对象,所以在调用A的函数的时候就不会有问题了.

4 . Heap vs stack
    * stack: 存放临时变量,函数参数,自动会分配和回收, 速度快, 空间有限通常就几 MB.
    * heap: 用于动态分配内存,通过new/malloc, 灵活但需要手动释放,内存泄漏会有大问题, 速度相对较慢

## Operation System

1. SpinLock, Mutex, Semaphore
    * SpinLock: 自旋锁, 这个东西只会用于一个非常简单的逻辑上,因为他要占用非常大的CPU, 如果你锁定的东西要执行很长时间,比如中间有网络IO/磁盘IO, 共享内存之类的操作,就不适合用这种自旋锁
    他的大概实现逻辑是这样的:自旋锁busy-waiting机制, 这个锁被其他线程持有,这个自旋锁就会一直循环去锁定,直到他锁上为止,这样会非常消耗CPU.常见实现 TAS(Test-and-Set)或者CAS(Compare-and-Swap).如果有兴趣可以看这个文章 [自旋锁](../SpinLock.md)

    * Mutex : 互斥锁, 这个锁的目标是试图去占有, 如果线程能够获取占有权,就进入锁成功,执行后面的逻辑,如果占有失败,就进入阻塞状态,有操作系统负责调度,唤醒与上下文切换.这不会严重消耗CPU资源,一般用于线程对一个变量加锁.另外他提供了try_lock, 进入了一种非阻塞尝试,这样会整个过程类似spinLock一样.

    * Semaphore:信号量, 它是一个带有计数器的同步对象.管理可用资源的数量, 例如计数为3 表示最多允许3个线程同时访问共享资源.他有两个核心的操作:P (wait()),就是当计数>0 的时候则技术减一,并且技术,否则阻塞线程知道被signal()唤醒, 另外一个V(signal()):计数加1,并且唤醒一个或者多个等待中的线程, 一般用作控制并发访问数量或者事件通知. 比如: 生产者--消费者中经常使用读者为wait(). 生产者signal()

    | 类型          | 是否有所有权  | 其他线程可进行解锁/释放？   | 典型用途           |
    | ------------- | ------- | --------------- | -------------- |
    | **Spinlock**  | ❌ 没有所有权 | ✅ 可以（只是原子标志位复位） | 临界区极短，无条件抢占锁时  |
    | **Mutex**     | ✅ 持有者独占 | ❌ 不可，必须由锁持有者解锁  | 严格互斥，正确清理资源    |
    | **Semaphore** | ❌ 没有所有权 | ✅ 可以被非操作线程释放    | 用于信号通知、生产者/消费者 |


2. Deadlock, Race Conditions
    * Deadlock: 死锁, 发生在多线程中,一个线程锁住A等待B, 另外一个线程锁住B等待A, 这样两个现成就永久阻塞了. 他有四个必要条件:
        * 互斥(mutex): 一个资源被一个线程独占
        * 占有并且等待(hold and wait): 线程持有资源时继续请求其他资源
        * 不可抢占(no preemption): 资源不能被外力强制回收
        * 环路等待(circular Wait): 形成一个资源等待环

        预防策略:
        * 禁止占有并且等待: 一次性申请所有的资源
        * 避免不可抢占, 一个资源抢占以后需要其他资源, 必须先放掉这个资源
        * 避免抢占,用一种方法拷贝数据避免抢占
        * 禁止环路等待: 大家用同样的顺序来锁定 

    * Race Conditions: 凡是访问共享数据都需要原子操作, 加锁,临界区尽可能小,避免更多串行执行.如果有复杂逻辑最好使用消息队列或者actor模式降级并发错误率.
    关于异步处理的设计模式在这里有详细说明 [异步处理的模式](../AsyncMode.md)

3. Thread synchronization

操作系统的,多进程,多线程, 数据库, TCP/IP, UDP, HTTP, SSL/TLS, 

## Game Develop

1. Game Loop

2. Delta Time

3. Frame, VSync (渲染管线基础)

4. Entity-Component-System 架构

5. Git版本控制 如何解决多人写作时候的合并冲突

6. 单元测试/调试 TDD思路

7. 架构设计, 设计一个模块让他可以在多人协作下容易扩展


## Other knowledge

1. Design pattern
    * Factory
    * Observer
    * State
    * ECS
    * Component
