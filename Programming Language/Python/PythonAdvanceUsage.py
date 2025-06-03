def log(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@log
def greet(name):
    print(f'Hello, {name}')


def func(n):
    i = 0
    while i<n:
        yield i
        i+=1

gen = func(100)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



def my_coro():
    while True:
        value = yield
        print("Received:", value)

v = my_coro()
next(v)
v.send("ASDFASDFA")
v.send(233)



import asyncio

async def greet():
    await asyncio.sleep(1)
    print("Hello async!!")

asyncio.run(greet())