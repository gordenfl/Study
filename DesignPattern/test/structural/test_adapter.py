import unittest
from Structural import Adapter


class TestAdapter(unittest.TestCase):
    def test_EnemyTank(self):
        tank = Adapter.EnemyTank()
        self.assertEqual(tank.fireWeapon(),
                         "Enemy Tank fire and get damage of ")
        self.assertEqual(tank.driveForward(), "Enemy Tank move forward")
        self.assertEqual(tank.assignDriver(), "Enemy Tank assign a driver")

        robot = Adapter.EnemyRobot()
        robot_tank = Adapter.EnemyRobotAdapter(robot)
        self.assertEqual(robot_tank.fireWeapon(),
                         "Enemy Robot attach with hand")
        self.assertEqual(robot_tank.driveForward(), "Enemy Robot walk forward")
        self.assertEqual(robot_tank.assignDriver(),
                         "Enemy robot tramps on human")
