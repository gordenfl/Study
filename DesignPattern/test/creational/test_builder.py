import unittest
from Creational import Builder


class TestBuilder(unittest.TestCase):
    def test_makeDellComputer(self):
        dellcomputer = Builder.DellComputerBuilder().getComputer()
        self.assertAlmostEqual(dellcomputer.getName(), "Dell Computer")
        self.assertAlmostEqual(dellcomputer.getDisk(), "Old SSD")
        self.assertAlmostEqual(dellcomputer.getMem(), "8G")
        self.assertAlmostEqual(dellcomputer.getDisplay(),
                               "DELL LED 16inch Display")

    def test_makeAppleComputer(self):
        applecomputer = Builder.AppleComputerBuilder().getComputer()
        self.assertAlmostEqual(applecomputer.getName(), "Apple Computer")
        self.assertAlmostEqual(applecomputer.getDisk(), "Apple SSD")
        self.assertAlmostEqual(applecomputer.getMem(), "64G")
        self.assertAlmostEqual(applecomputer.getDisplay(),
                               "Apple Retation 17inch LED")
