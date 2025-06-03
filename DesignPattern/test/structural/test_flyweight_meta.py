import unittest
from Structural import FlyweightMeta

class TestFlyweightMeta(unittest.TestCase):
    def test_FlyweightMeta(self):
        c1 = FlyweightMeta.Card('9', 'h')
        c2 = FlyweightMeta.Card('9', 'h')
        self.assertEqual(c1, c2)
        
        self.assertEqual(len(FlyweightMeta.Card._pool), 1)
        
        c3 = FlyweightMeta.Card("23", "ASDFASDFASDF")
        self.assertEqual(c1, c2)
        self.assertNotEqual(c3, c1)
        
        self.assertEqual(len(FlyweightMeta.Card._pool), 2)
        
        c1.new_attr = "ASDFA"
        c4 = FlyweightMeta.Card('9', 'h')
        self.assertTrue(hasattr(c2, 'new_attr'))

        FlyweightMeta.Card._pool.clear()
        c4 = FlyweightMeta.Card('9', 'h')
        self.assertFalse(hasattr(c4, 'new_attr'))


