class FlyType(object):
    def fly(self):
        pass


class ItFly(FlyType):
    def fly(self):
        return True, "can fly"


class CantFly(FlyType):
    def fly(self):
        return False, "can not fly"


class Animal(object):
    def __init__(self):
        self.name = ""
        self.flytype = None

    def canFly(self):
        pass

    def setFly(self, flytype):
        self.flytype = flytype


class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        self.flytype = CantFly()

    def canFly(self):
        ret, strs = self.flytype.fly()
        return ret


class Bird(Animal):
    def __init__(self):
        super(Bird, self).__init__()
        self.flytype = ItFly()

    def canFly(self):
        ret, strs = self.flytype.fly()
        return ret
