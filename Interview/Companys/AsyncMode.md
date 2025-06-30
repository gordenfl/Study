# Async Modes

This is a table about all Async Modes during all product we can use:
| 模式                   | 用途 / 解决问题       | 核心机制              |
| -------------------- | --------------- | ----------------- |
| Producer-Consumer    | 解耦生产消费、缓冲处理     | 阻塞队列 + 信号量/互斥     |
| Thread Pool          | 限制并发线程数量，提高效率   | 线程复用              |
| Future/Promise       | 异步调用 + 等待结果     | 提交任务 + `Future`   |
| Reactor/Proactor     | 高并发 I/O 事件处理    | I/O 多路复用 / 异步 I/O |
| Fork–Join            | 并行拆分任务处理        | 递归分叉合并结果          |
| Reader–Writer Lock   | 读多写少提高并发性能      | 读并发 + 写互斥         |
| Barrier/Rendezvous   | 控制并发同步点         | 所有线程等待后统一释放       |
| Active Object        | 异步请求封装 + 顺序处理   | mailbox + 代理线程    |
| Monitor              | 结构化同步/条件等待      | 方法内锁 + 条件变量       |
| Thread-local Storage | 避免共享冲突、保持线程独立状态 | 各线程独立存储           |


## Producer-Consumer 模型

这里面管理一个任务队列,任何生产者产生任务都放入缓冲队列, 每个消费者线程都会从队列中获取一个任务并且处理, 配合信号量Semaphore 来做限制, 需要在缓冲队列中取数据的时候加上线程安全.就是说让这个任务队列里面有一个线程安全的Mutex, 保证他们在取数据的时候是一个一个取的,这样就不会产生两个Consumer获取到同一个数据.

## 线程池 Thread-pool

创建固定数量的线程,反复处理任务,避免频繁创建和销毁, 适用于大量短任务并发场景, 提升资源利用率, 

## Future/Promise/Async Method Invocation

提交一个异步任务, 就是一个Future,然后立即返回, 去做其他事情. 你的立即会在后面通过Future.get()等方式来获取结果, 非阻塞模式调用,常见于网络请求或后台任务. Javascript中的Promise就是这种做法, 其中有.then, await, .cache等获取未来结果. 不会阻塞住主线程.

## Reactor/Proactor

Reactor: 基于事件循环(I/O multiplexer 如: epoll/select), 同步分发事件并且调用响应处理的函数
Proactor: 异步I/O完成的时候由框架通知用户逻辑, 适合高性能网络服务器
网络游戏的服务器基本就是这样的

## Fork-Join(分叉-合并)

将任务递归拆分成多个子任务并且执行, 完成后再汇总结果, Java ForkJoinPoll 就是这个模式的成熟实现.注意一点就是尽量的将你的线程执行的任务细分.这样会让你线程和线程之间减少依赖关系,会让程序更快.推荐是不同享数据, 在Join的时候汇总数据.
ThreadLocal 用这种方法将线程共享的数据复制到每个线程,他们自己来管理,这样就不会有冲突的形成,比如database session, request context 这种东西,举个例子:
```CPP
#include <iostream>
#include <thread>

thread_local int tls_var = 0;

void worker(int id) {
    tls_var = id;
    std::cout << "Thread " << id << " tls_var = " << tls_var << "\n";
}

int main(){
    std::thread t1(worker, 1);
    std::thread t2(worker, 2);
    t1.join(); t2.join();
}
```
这样每个线程在访问tls_var的时候就是自己的, 因为```thread_local int tls_var = 0;``` 这里的thread_local就是给你设置了这个属性.

## Reader-Writer Lock(读写锁)

支持多个读者并发访问,单写者互斥; 适合 "读多写少"的场景, 提高并发性能. 比如:缓存系统, 配置管理系统

## Barrier(屏障)/Rendezvous(汇合点)

Barrier: 让多个线程汇总澡一个同步点再一起继续
Rendezvous: 两个线程在格子执行到一定阶段后,互相等待并且同步, 然后再继续
举例:
并行计算,在分布式计算中,每个层级的计算需要等所有任务都完成,然后汇合所有结果返回给上一层

## Active Object

将请求封装成为消息,提交给自身线程执行, 类似Actor, 但是带上代理, 提供同步接口, 常用于一步任务封装

## Monitor (监视对象)

类/对象 内部封装锁和条件变量, 其方法保证在锁保护下运行,常见的Java synchronized 和 C++ std::condition_variable

## Thread-local Storage (线程本地存储)

每个线程有独立的数据副本, 避免竞争, 适合每个线程保持独立的状态场景, 减少同步开销,前面说到的 Thread_Local的用法就是这样, 将数据都复制到自己线程中来做运算.

## 其他模式 TODO

Double-Checked Locking: 结合懒初始化和锁优化, Balking, Guarded Suspension, Leaders/Follower, Scheduler, Nuclear Reaction 等
