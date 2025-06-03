# 多线程

Python中的多线程是一个很鸡肋的功能,现在详细描述一下Python的Multi Threading他内部的实现:

Threading 本身就是启动了一个操作系统层面上的Thread, 并且让其运行,在Python下面的Thread每次要执行代码的时候,必须要先获取一个GIL 才能够执行,也就是说所有的Thread 都需要等待着去获取GIL, 拿到GIL的thread 就可以去执行,即使这台服务器上存在多个CPU core 也不行.

Python的这个鸡肋的Thread 功能让人非常难受.所以在3.5 以后开发了一个叫做asyncio的功能,就像Lua中的coroutine, 他可以做到让Python虚拟机在单线程里面同时做很多事情,这样高效的做法被很多的并行量非常大的需求而用上.

## 多线程:
    先不考虑Python语言,我们理解的多线程是包含在一个进程中的多个可执行单元,可以同时使用一个CPU的多核,同时处理问题,如果你用C++来写代码就可以保证同时执行,但是这其中有一点非常重要的就是需要保证数据的安全性,这样你就需要用到一些mutex, atomic Semphone 等来对一些关键数据进行加锁,避免两个进程同时访问一个变量后导致运算错误.
    
    而在Python中的Multi thread 则使用的是 一个叫GIL 的东西,他规定在Python中创建的线程,Python会自动给你创建一个操作系统级别的Thread, 但是如果每一个Thread 需要执行代码的话,需要让P这个thread 先获取GIL 才行,这言下之意就是说, Python的多线程看起来产生了多个线程,实际上做事情的只有那个获得了GIL的一个线程.而且创建线程的开销非常大.这就带来了低效.


## 如何解决问题
    asyncio, aoihttp
    这些库在2015年发布以后,提高了很多HTTP效率.他的原理是这样的:
    Python 代码如果使用了asyncio 的, 他就会在这个线程中分出多个task, 这些task 在这个线程中轮询执行,这样不用切换Python解释器的上下文就大幅提高了代码的执行效率,虽然是单线程但是比过去的多线程要快很多.

    具体的样例:
    
    ```python
    import asyncio
    import aiohttp
    import time

    URLS = [
        "https://httpbin.org/delay/1" for _ in range(10)
    ]

    async def fetch(session, url):
        async with session.get(url) as response:
            text = await response.text()
            print(f"✅ Done: {url}")
            return text

    async def main():
        async with aiohttp.ClientSession() as session:  # 用aiohttp 创建多个Clientsession, 可以看做是多个任务
            tasks = [fetch(session, url) for url in URLS] #每个任务调用fetch
            await asyncio.gather(*tasks)

    if __name__ == "__main__":
        start = time.time()
        asyncio.run(main())
        print(f"⏱ Total time: {time.time() - start:.2f} seconds")
    ```

    解释一下这段代码的目标是同时fetch URLS 里面10个URL的内容,然后返回.
    如果用Thread来做的话,需要for循环来创建threading.Thread(....) 然后让每个thread去执行,其实也还是串行去执行的,但是线程调度会让上下文切换,导致效率很低. 这里则不需要切换.在一个线程中同时去执行10个任务,10个任务其基本上可以感觉是同时完成.

    如果是多个网站需要不同的header 去访问,也可以使用同一个session, 只需要在session.get后面增加headers=headers 你定义一个header 就可以了:
    ```python
    headers = {"Authorization": f"Bearer {token}"}
    async with session.get("https://api.example.com/user/info", headers=headers) as resp:

    ```


    Useful for all the Async logic.