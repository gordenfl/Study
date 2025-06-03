import unittest

from Behavioural import Visitor


class VisitorTest(unittest.TestCase):
    def test_visitor(self):
        normal_tax = Visitor.TaxVisitor()  # 1.1 1.3 1
        holiday_tax = Visitor.TaxHolidayVisitor()  # 1.2 1.5 1.1

        l1 = Visitor.Liquor(100)
        self.assertEqual(l1.accept(normal_tax), 110)
        self.assertEqual(l1.accept(holiday_tax), 120)

        l2 = Visitor.Tobaco(200)
        self.assertEqual(l2.accept(normal_tax), 260)
        self.assertEqual(l2.accept(holiday_tax), 300)

        l3 = Visitor.Necessity(500)
        self.assertEqual(l3.accept(normal_tax), 500)
        self.assertEqual(l3.accept(holiday_tax), 550)
