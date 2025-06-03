# 这个设计模式是用来构造类似编辑器内容管理这类结构的

# 这个是用来存储历史数据的
class Memento(object):
    def __init__(self, article):
        self.article = article

    def getArticle(self):
        return self.article

# 这个是用来给外边显示用的


class Originator(object):
    def __init__(self):
        self.article = None

    # 设置临时数据的
    def setArticle(self, article):
        self.article = article

    # 存储到历史数据中
    def storeIntoMemento(self):
        return Memento(self.article)

    # 从历史数据中恢复回来
    def restoreFromMemento(self, memento):
        self.article = memento.getArticle()
        return self.article


class CareTaker(object):
    def __init__(self):
        self.savedArticles = []  # arraylist of Memento

    def addMemento(self, m):  # argument is type of Memento
        self.savedArticles.append(m)

    def getMemento(self, index):  # return type of Memento
        if index < 0 or index >= len(self.savedArticles):
            return None
        return self.savedArticles[index]


class TestMemento(object):
    def __init__(self):
        self.currentVersion = 0
        self.totalVersion = 0
        self.careTaker = CareTaker()  # 用来存储用的
        self.originator = Originator()  # 用来显示用的

    def getArticle(self):  # return string
        return self.originator.article

    def getCurrentVersion(self):
        return self.currentVersion

    def getTotalVersion(self):
        return self.totalVersion

    def save(self):
        m = self.originator.storeIntoMemento()  # generator a new Memento Object
        self.careTaker.addMemento(m)
        self.totalVersion += 1
        self.currentVersion += 1
        return m

    def undo(self):
        if self.currentVersion == 0:
            return False
        self.currentVersion -= 1
        m = self.careTaker.getMemento(self.currentVersion)
        self.originator.setArticle(m)
        return True

    def redo(self):
        if self.currentVersion == self.totalVersion:
            return False

        self.currentVersion += 1
        m = self.careTaker.getMemento(self.currentVersion)
        self.originator.setArticle(m)
        return True
