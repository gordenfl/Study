# Go 

## Basic knowledge

[ Here ](./proj1/PROJ1.md)

## Go Kernel and Deeper

1. goroutine: you know the lua coroutine and python asyncio. it's the same. easy to understand. 协程

    ```go
    go func() {
        time.Sleep(time.Second)
        fmt.Println("goroutine done")
    }()
    ```

2. channel - sync data bridge between goroutine TODO: know more detail

    ```go
    ch := make(chan int)
    go func() {
        ch <- 42  // 若无人接收，此处 goroutine 阻塞
    }()
    value := <-ch  // 等待接收
    ```

3. sync - Mutex, 等待组 : TODO: 一个函数返回了以后并没有unLock会发生什么?

    ```go
    var mu sync.Mutex
    mu.Lock()
    mu.Unlock()
    ```

4. worker pool - limit of concurrent, task management  TODO: code does not understand yet.

    ```go
    jobs := make(chan int, 100)
    results := make(chan int, 100)
    for w := 0; w < 5; w++ {
        go worker(w, jobs, results)
    }
    ```

    it can generate specific count of worker to do something, this code sample is too easy, TODO: to understand more

5. fan-out/fan-in - Extend concurrent, aggregation all the result

    ```go
    for i := 0; i < 10; i++ {
        go func(i int) { results <- doWork(i) }(i)  // fan-out
    }
    for i := 0; i < 10; i++ {
        res := <-results  // fan-in
        fmt.Println(res)
    }
    ```

    the code is too simple TODO: make more detail to understand.

6. Deadlock - all goroutine block



## Framework and System Design

## Network and API 

## Data Storage and Middleware

## DevOps and Deploy