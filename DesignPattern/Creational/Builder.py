class Computer(object):
    def __init__(self, name=None, CPU=None, Mem=None, Display=None, Disk=None):
        self.name = name
        self.CPU = CPU
        self.Mem = Mem
        self.Display = Display
        self.Disk = Disk

    def getInfo(self):
        return "name:%s\n CPU:%s\n Mem:%s\n Display:%s\n Disk:%s\n" % (
            self.name,
            self.CPU,
            self.Mem,
            self.Display,
            self.Disk,
        )

    def getName(self):
        return self.name

    def getDisk(self):
        return self.Disk

    def getMem(self):
        return self.Mem

    def getDisplay(self):
        return self.Display


class ComputerBuilder(object):
    DEFAULT_COMPUTER = {
        "name": "Common Computer",
        "CPU": "Intel 2.4GHz",
        "Mem": "16G",
        "Display": "DELL 19 inch LED",
        "Disk": "Samsum 1T SSD",
    }

    def __init__(self):
        self.last_computer = None

    def getName(self):
        return ComputerBuilder.DEFAULT_COMPUTER["name"]

    def getCPU(self):
        return ComputerBuilder.DEFAULT_COMPUTER["CPU"]

    def getMem(self):
        return ComputerBuilder.DEFAULT_COMPUTER["Mem"]

    def getDisplay(self):
        return ComputerBuilder.DEFAULT_COMPUTER["Display"]

    def getDisk(self):
        return ComputerBuilder.DEFAULT_COMPUTER["Disk"]

    def getComputer(self):
        self.last_computer = Computer(
            name=self.getName(),
            CPU=self.getCPU(),
            Mem=self.getMem(),
            Display=self.getDisplay(),
            Disk=self.getDisk(),
        )
        return self.last_computer


class AppleComputerBuilder(ComputerBuilder):
    def getName(self):
        return "Apple Computer"

    def getDisk(self):
        return "Apple SSD"

    def getMem(self):
        return "64G"

    def getDisplay(self):
        return "Apple Retation 17inch LED"


class DellComputerBuilder(ComputerBuilder):
    def getName(self):
        return "Dell Computer"

    def getDisk(self):
        return "Old SSD"

    def getMem(self):
        return "8G"

    def getDisplay(self):
        return "DELL LED 16inch Display"
