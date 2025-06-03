import unittest

from Behavioural import Responsibility


class ResponsibilityTest(unittest.TestCase):
    def test_responsibility(self):
        add = Responsibility.AddNumber()
        sub = Responsibility.SubNumber()
        mul = Responsibility.MulNumber()
        div = Responsibility.DivNumber()
        add.setNext(sub)
        sub.setNext(mul)
        mul.setNext(div)

        chain = add

        action = Responsibility.Numbers(1, 2, "+")
        self.assertEqual(chain.do(action), "1+2=3")
        action = Responsibility.Numbers(1, 2, "*")
        self.assertEqual(chain.do(action), "1*2=2")
        action = Responsibility.Numbers(1, 2, "*")
        self.assertEqual(chain.do(action), "1*2=2")
        action = Responsibility.Numbers(1, 2, "/")
        self.assertEqual(chain.do(action), "1/2=0")

        action = Responsibility.Numbers(1, 2, "#")
        self.assertEqual(chain.do(action), "we can not deal with action of #")
