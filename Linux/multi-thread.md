# Lock about the multi-thread

## spin lock

This is a lock alway testing whether it can be locked, without any time wait. it will have CPU cost, and alway using for the simple logic lock, such like: no disk io, no network, only have cpu operation.

## mutex

Mutex is a lock alway been used. It will test whether the object has been lock by other mutex, if yes, this lock will waiting for sometime, after that it will retry to lock that resource, but only on mutex can only lock one resource to let one visitor to use the resource. because some time will waiting between two times retry. It' will not cost so much CPU usage.

Only the thread who create the mutex can free it. other thread can not. it always used for share resource visiting.

## semaphore

Semaphore: is another kind of lock, semaphore, can only lock one resource. but it has different with mutex is semaphore has a limitation in it. limitation means that semaphore can have more lockers to lock this resource it until the count achieve to limitation, semaphore can not let other logic lock.

any thread can free semaphore. it only use for the control the number of concurrent connection.