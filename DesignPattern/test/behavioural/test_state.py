import unittest

from Behavioural import State


class StateTest(unittest.TestCase):
    def GetResult(self, machine, commands):
        ret = []
        for c in commands:
            if c == "1":
                ret.append(machine.InsertCoin())
            elif c == "2":
                ret.append(machine.EjectCoin())
            elif c == "3":
                ret.append(machine.PushButton())
            elif c == "4":
                ret.append(machine.DispenseChocolate())
            elif c == "5":
                ret.append(machine.AddChocolate())
            else:
                ret.append(False)
        return ret

    def test_State(self):
        machine = State.VendingMachine()
        ret = self.GetResult(machine, "123123")
        target = [True, True, False, True, True, False]
        for i in range(len(target)):
            v = ret[i]
            self.assertEqual(v, target[i])
        return

    def test_State2(self):
        machine = State.VendingMachine()
        ret = self.GetResult(machine, "134134134134134134134134134134151")
        target = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                  True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True]
        #print(ret, target)
        for i in range(len(target)):
            v = ret[i]
            self.assertEqual(v, target[i])
        #self.assertEqual(machine.ProductCount, 0)
        return
