#############  product As##########################
class AbstractProductA(object):
    def doExecute(self):
        return "ProductA Super, execute"


class ProductA1(AbstractProductA):
    def doExecute(self):
        return "ProductA1, execute"


class ProductA2(AbstractProductA):
    def doExecute(self):
        return "ProductA2, execute"

#############  product Bs###########################


class AbstractProductB(object):
    def doExecute(self):
        return "ProductB Super, execute"


class ProductB1(AbstractProductB):
    def doExecute(self):
        return "ProductB1, execute"


class ProductB2(AbstractProductB):
    def doExecute(self):
        return "ProductB2, execute"


class AbstractFactory(object):
    def createProductA(self):
        assert 1 == 2

    def createProductB(self):
        assert 1 != 1


class ConcreateFactor1(AbstractFactory):
    def createProductA(self):
        return ProductA1()

    def createProductB(self):
        return ProductB2()


class ConcreateFactor2(AbstractFactory):
    def createProductA(self):
        return ProductA2()

    def createProductB(self):
        return ProductB2()


class ConcreateFactor3(AbstractFactory):
    def createProductA(self):
        return ProductA1()

    def createProductB(self):
        return ProductB1()


def TestCase(FactorObj):
    ObjectA = FactorObj.createProductA()
    ObjectB = FactorObj.createProductB()
    ObjectA.doExecute()
    ObjectB.doExecute()
