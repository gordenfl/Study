class NativeProxy(object):
    @staticmethod
    def getAttrName():
        return "__target__"

    def __init__(self, target):
        assert(target)
        object.__setattr__(self, NativeProxy.getAttrName(), target)
        self.vvv = 1

    def __getattribute__(self, item):
        try:
            target = object.__getattribute__(self, item)
            if isinstance(target, type(object().__str__)):  # wrapped method
                print("-====")
                raise AttributeError
            else:# 这里获取 NativeProxy 本身的属性 Attribute
                print("ADSFASDFASDF", target)
                return target
        except AttributeError:
            target = object.__getattribute__(self, NativeProxy.getAttrName())
            return getattr(target, item)

    def __setattr__(self, key, value):
        """修改set逻辑"""
        target = object.__getattribute__(self, NativeProxy.getAttrName())
        if key in dir(target): #这里修改NativeProxy 本身的属性
            setattr(target, key, value)
        else:#这里修改受到代理的对象的属性
            object.__setattr__(self, key, value)


class Teacher(object):
    def __init__(self):
        self._name = None
    #_name = None

    def getTeacherName(self):
        return self._name

    def setTeacherName(self, name):
        self._name = name


if __name__ == '__main__':
    teacher = Teacher()
    p_teacher = NativeProxy(teacher)
    p_teacher.vv = 342
    p_teacher.setTeacherName("Gordon")
    print("Teacher Name:", p_teacher.getTeacherName(), teacher.getTeacherName())
    p_teacher.setTeacherName("TTTTTTTT")
    print("Teacher Name:", p_teacher.getTeacherName(), teacher.getTeacherName())
    print(p_teacher.vv, "---")
