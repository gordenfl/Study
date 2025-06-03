from abc import ABC, abstractmethod

# 就是Clone 函数， 用一个已经存在的对象，创建一个新的对象，借鉴已经存在对象的一些特定的属性


class CloneableItem(object):  # item in online game server
    def __init__(self, name=None):
        self.name = name
        self.cloned = False

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def clone(self):
        pass


class EquipItem(CloneableItem):
    def __init__(self, name=None):
        super().__init__(name)

    def getName(self):
        return self.name

    def clone(self):
        obj = EquipItem()
        obj.name = self.name+" cloned"
        obj.cloned = True

        return obj


class StoneItem(CloneableItem):
    def __init__(self, name):
        super().__init__(name)

    def getName(self):
        return self.name

    def clone(self):
        obj = StoneItem(self)
        self.name = equip.name+" cloned"
        self.cloned = True
        return obj
