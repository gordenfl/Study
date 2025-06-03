import unittest

from Behavioural import TemplateMethod


class TemplateMethodTest(unittest.TestCase):
    def test_templatemethod(self):
        #pizza = FullPizza(Pizza.PIZZA_LARGE)
        domino = TemplateMethod.DominoPizzaStore()
        address = "10 silver lace ct, San Rafael, CA 94903"
        pizza = domino.MakePizza(
            TemplateMethod.Pizza.PIZZA_TYPE["MEAT"], TemplateMethod.Pizza.PIZZA_SIZE["MEDIA"], address)
        self.assertNotEqual(pizza, None)
        self.assertEqual(pizza.getCheese(), False)
        self.assertEqual(pizza.getMeat(), True)
        self.assertEqual(pizza.getPrice(), 15)

        pizza = domino.MakePizza(
            TemplateMethod.Pizza.PIZZA_TYPE["CHEESE"], TemplateMethod.Pizza.PIZZA_SIZE["MEDIA"], address)
        self.assertNotEqual(pizza, None)
        self.assertEqual(pizza.getCheese(), True)
        self.assertEqual(pizza.getMeat(), False)
        self.assertEqual(pizza.getPrice(), 10)

        pizza = domino.MakePizza(
            TemplateMethod.Pizza.PIZZA_TYPE["FULL"], TemplateMethod.Pizza.PIZZA_SIZE["MEDIA"], address)
        self.assertNotEqual(pizza, None)
        self.assertEqual(pizza.getCheese(), True)
        self.assertEqual(pizza.getMeat(), True)
        self.assertEqual(pizza.getPrice(), 25)
