import unittest
from Creational import Prototype


class TestPrototype(unittest.TestCase):
    def testClone(self):
        equip = Prototype.EquipItem("Equip")
        equip_clone = equip.clone()
        self.assertNotEqual(equip, equip_clone)
        self.assertEqual(equip_clone.cloned, True)
        self.assertEqual(type(equip), type(equip_clone))
