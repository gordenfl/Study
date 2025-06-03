import unittest
from Structural import Composite


class TestAdapter(unittest.TestCase):
    def test_Adapter(self):
        netease = Composite.CompanyInfo("netease")
        netease.addEmployee(Composite.Developer(
            1, "Gordon", "C#/.NET Developer"))
        netease.addEmployee(Composite.Manager(2, "Oneqiong", "CEO"))
        netease.addEmployee(Composite.Developer(
            3, "Bing", ".NET Developer (Device Integration)"))

        self.assertEqual(netease.getEmployee(
            1).showEmployeeInfo(), "Developer Info, Id:%d, Name:%s, Position:%s" % (1, "Gordon", "C#/.NET Developer"))
        self.assertEqual(netease.getEmployee(
            2).showEmployeeInfo(), "Manager Info, id:%d, Name:%s, Position:%s" % (2, "Oneqiong", "CEO"))
        self.assertEqual(netease.getEmployee(5), None)
