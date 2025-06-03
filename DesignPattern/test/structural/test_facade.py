import unittest
from Structural import Facade


class TestFacade(unittest.TestCase):
    def test_facade(self):
        computer = Facade.Computer()
        computer.Start()

        log = computer.getLog()
        target_log = [
            "CPU: freezed",
            "HardDrive: read some data form somewhere from Hard drive",
            "Memory: load some data",
            "CPU: Jump to somewhere",
            "CPU: execute some command"
        ]
        self.assertEqual(len(log), len(target_log))
        for i in range(len(log)):
            self.assertEqual(log[i], target_log[i])
        return
