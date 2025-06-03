# 把若干对象整合成一个对象，由这个对象提供对外的统一接口
class ComputerComponent(object):
    def __init__(self):
        pass


class CPU(ComputerComponent):
    def Freeze(self):
        return "CPU: freezed"

    def Jump(self):
        return "CPU: Jump to somewhere"

    def Execute(self):
        return "CPU: execute some command"


class Memory(ComputerComponent):
    def Load(self, data):
        return "Memory: load some data"

    def Read(self):
        return "Memory: read some data form memory"


class HardDrive(ComputerComponent):
    def Read(self):
        return "HardDrive: read some data form somewhere from Hard drive"

    def Write(self):
        return "HardDrive: Write some data into hard drive some place"


class Computer(ComputerComponent):
    def __init__(self):
        super().__init__()
        self.cpu = CPU()
        self.memory = Memory()
        self.harddrive = HardDrive()
        self.log = []

    def getLog(self):
        return self.log

    def Start(self):
        ret = self.cpu.Freeze()
        self.log.append(ret)

        ret = self.harddrive.Read()
        self.log.append(ret)

        ret = self.memory.Load(ret)
        self.log.append(ret)

        ret = self.cpu.Jump()
        self.log.append(ret)
        ret = self.cpu.Execute()
        self.log.append(ret)
