import unittest
from Creational import AbstractFactory


class TestProductFactory(unittest.TestCase):
    def test_factory1(self):
        factory1 = AbstractFactory.ConcreateFactor1()
        objA = factory1.createProductA()
        objB = factory1.createProductB()
        self.assertAlmostEqual(objA.doExecute(), "ProductA1, execute")
        self.assertAlmostEqual(objB.doExecute(), "ProductB2, execute")
        return objA.doExecute(), objB.doExecute()

    def test_factory2(self):
        factory2 = AbstractFactory.ConcreateFactor2()
        objA = factory2.createProductA()
        objB = factory2.createProductB()
        self.assertAlmostEqual(objA.doExecute(), "ProductA2, execute")
        self.assertAlmostEqual(objB.doExecute(), "ProductB2, execute")

    def test_factory3(self):
        factory3 = AbstractFactory.ConcreateFactor3()
        objA = factory3.createProductA()
        objB = factory3.createProductB()
        self.assertAlmostEqual(objA.doExecute(), "ProductA1, execute")
        self.assertAlmostEqual(objB.doExecute(), "ProductB1, execute")
