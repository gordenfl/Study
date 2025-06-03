import unittest

from Behavioural import Strategy


class StrategyTest(unittest.TestCase):
    def test_strategy(self):
        dog = Strategy.Dog()
        self.assertEqual(dog.canFly(), False)
        bird = Strategy.Bird()
        self.assertEqual(bird.canFly(), True)
        dog.setFly(Strategy.ItFly())
        self.assertEqual(dog.canFly(), True)
