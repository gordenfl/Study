import unittest

from Structural import Decorator

class TestDecorator(unittest.TestCase):
    def test_Decorator(self):
        pizza = Decorator.PeppyPaneer()
        self.assertEqual(pizza.getDescription(), "Peppy Paneer")
        self.assertEqual(pizza.getCost(), 20)
        
        new = Decorator.Barbeque(Decorator.FreshTomato(Decorator.Onion(Decorator.FarmHouse())))
        self.assertEqual(new.getDescription(), "Farm House"+", Onion"+", Fresh tomato"+", Barbeque")