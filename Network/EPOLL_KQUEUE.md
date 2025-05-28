# EPOLL && KQUEUE

## EPOLL

epoll is only support for Linux system. compared with select and poll, it has some different and good aspect:

1. it can support large amount file descriptions(FD)
2. event driven, it use the event from system kernel. avoid to check each fd that is most low efficient part of select and poll.
3. support ET and LT two mode. ET (Edge Triggered), LT (Level-Triggered)

### ET vs LT

* LT is default mode. The logic like poll, epoll_wait will return while the fd is ready.
* ET is different. The logic is that, epoll_wait will return it once. after that, if the fd still ready, it will not return. So please keep your logic deal all fd after epoll_wait returns all the fds.

### Advantage

* support the many fd (2^31-1), it's efficiency to manage large mount of fds.
* Traversal Linked List in the kernel. Don't go through all the linked list in the user mode.
* ET mode will reduce notify. Hight efficient such like : Nginx, Redis use it

### Disadvantages

* You must read or write in a loop until get EAGAIN , otherwise message will be lost.
* EPOLLONESHOT: only give notice once. It fit for multi thread mode. Don't deal with same fd with different thread.
* epoll maybe not faster than select, if fd is not so much, select/poll maybe faster then epoll

## KQUEUE

kqueue is only supported on BSD (MacOS, FreeBSD). It provide a high efficient event way.
Kqueue create a kernel event queue. you can:

* kqueue() : create an queue
* kevent() : register/modify/delete event, or waiting event.

Kqueue is like epoll. It not only support fd event(read, write, error), but also support:

* Filesystem change notify
* Process event
* Signal
* Timer (don't need other thread)

How to trigger Kqueue: Kqueue will be trigger like ET in epoll.

### Advantages

* Many event can be support with Kqueue.
* Timer, Signal, Process Event can be trigger. It's better to using complex system
* It is more efficient than epoll. because less user mode system mode switch.

### Disadvantages

* you must deal with all the event till the EWOULDBLOCK
* There are some limitation on MacOS such as: it can not support FIFO file.
* it only support MacOS and FreeBSD not support Linux.
