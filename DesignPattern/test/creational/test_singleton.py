import unittest
from Creational import Singleton


class TestSingleton(unittest.TestCase):
    def test_Singleton(self):
        obj = Singleton.Singleton.getInstance()

        self.assertAlmostEqual(obj, Singleton.Singleton.getInstance())
