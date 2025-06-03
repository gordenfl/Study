
# static Proxy sample
class ITeacherInterface(object):
    def __init__(self):
        pass

    def doClass(self):
        pass


class TeacherDAO(ITeacherInterface):
    def __init__(self):
        pass

    def doClass(self):
        return "Teacher DAO make real class"


class TeacherDAOProxy(ITeacherInterface):
    def __init__(self, proxyObj=None):
        self.proxyObj = proxyObj

    def doClass(self):
        if not self.proxyObj:
            self.proxyObj = TeacherDAO()

        return self.proxyObj.doClass()
