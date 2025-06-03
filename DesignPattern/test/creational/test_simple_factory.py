import unittest
from Creational import SimpleFactory


class TestSimpleFactory(unittest.TestCase):
    def test_createProduct(self):
        factory = SimpleFactory.ProductFactory()

        obj = factory.creatorProduct1("ProductA")
        target_obj = SimpleFactory.ProductA()
        self.assertEqual(type(obj), type(target_obj))

        obj = factory.creatorProduct1("ProductB")
        target_obj = SimpleFactory.ProductB()
        self.assertEqual(type(obj), type(target_obj))

        obj = factory.creatorProduct1("ProductC")
        target_obj = SimpleFactory.ProductC()
        self.assertEqual(type(obj), type(target_obj))
