from types import MethodType


class InvocationHandler(object):
    def __init__(self, obj, func):
        self.object = obj
        self.func = func

    def __call__(self, *args, **kwargs):
        print('handler:', self.func, args, kwargs)
        print(self.func.__name__)
        return self.func(*args, **kwargs)


class HandlerException(Exception):
    def __init__(self, cls):
        super(HandlerException, self).__init__(cls, ' is not a handler class')


class Proxy(object):
    def __init__(self, cls, hcls):
        self.cls = cls
        self.hcls = hcls
        self.handlers = {}

    def __call__(self, *args, **kwargs):
        self.obj = self.cls(*args, **kwargs)
        return self

    def __getattribute__(self, name):
        print('get arrt:', name)
        isExist = hasattr(self.obj, attr)
        if not isExist:
            return None

        res = getattr(self.obj, attr)
        if isinstance(res, MethodType):
            if self.handlers.get(res) is None:
                self.handler[res] = self.hcls(self.obj, res)
            return self.handlers[res]
        else:
            return res


class ProxyFactory(object):
    def __init__(self, hcls):
        if issubclass(hcls, InvocationHandler) or hcls is InvocationHandler:
            self.hcls = hcls
        else:
            raise HandlerException(hcls)

    def __call__(self, cls):
        return Proxy(cls, self.hcls)


@ProxyFactory(InvocationHandler)
class Transaction:
    def __init__(self):
        pass

    def make_friend(self, a, b):
        print("hello", a, b)

    def reply(self, a):
        print('hello ', a)


t = Transaction()
pt = Proxy(t)
pt.make_friend(1, 2)
