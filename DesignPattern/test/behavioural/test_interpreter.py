import unittest

from Behavioural import Interpreter


class TestInterpreter(unittest.TestCase):
    def test_Interpreter(self):
        calc = Interpreter.Evaluator()
        v = calc.Parse("1 2 + 3 4 * 5 + -")
        self.assertEqual(v.Interpret(), -14)

    def test_Interpreter(self):
        calc = Interpreter.Evaluator()
        v = calc.Parse("9 8 - 15 + 5 * 2 /")
        self.assertEqual(v.Interpret(), 40)
