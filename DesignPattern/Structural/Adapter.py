from abc import ABC, abstractmethod, ABCMeta


class EnemyAttacker(metaclass=ABCMeta):
    @abstractmethod
    def fireWeapon(self):
        pass

    @abstractmethod
    def driveForward(self):
        pass

    @abstractmethod
    def assignDriver(self):
        pass


class EnemyTank(EnemyAttacker):
    def fireWeapon(self):
        return "Enemy Tank fire and get damage of "

    def driveForward(self):
        return "Enemy Tank move forward"

    def assignDriver(self):
        return "Enemy Tank assign a driver"


class EnemyRobot(object):
    def smashWithHands(self):
        return "Enemy Robot attach with hand"

    def walksForward(self):
        return "Enemy Robot walk forward"

    def reactToHuman(self):
        return "Enemy robot tramps on human"


class EnemyRobotAdapter(EnemyAttacker):
    def __init__(self, robot=None):
        if not robot:
            self.robot = EnemyRobot()
        else:
            self.robot = robot

    def fireWeapon(self):
        return self.robot.smashWithHands()

    def driveForward(self):
        return self.robot.walksForward()

    def assignDriver(self):
        return self.robot.reactToHuman()
