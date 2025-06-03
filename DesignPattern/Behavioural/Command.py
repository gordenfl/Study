from abc import ABC, ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class Command1(Command):
    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self):
        return "Command1 been executed on " + self.receiver.getName()


class Command2(Command):
    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self):
        return "Command2 been executed on " + self.receiver.getName()


class Command3(Command):
    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self):
        return "Command3 been executed on " + self.receiver.getName()


class InvokerCommand(object):
    def __init__(self, command):
        self.command = command

    def action(self):
        return self.command.execute()


class InvokerCommands(object):
    def __init__(self, command=None):
        self.commands = []
        if command:
            self.commands.append(command)

    def action(self):
        ret = []
        for command in self.commands:
            ret.append(command.execute())
        return ret

    def addCommand(self, command):
        self.commands.append(command)
