import unittest
from Behavioural import Command


class Student(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class TestCommand(unittest.TestCase):
    def test_command(self):
        invoker = Command.InvokerCommand(Command.Command1(Student("Gordon")))
        self.assertEqual(invoker.action(), "Command1 been executed on Gordon")

        invoker = Command.InvokerCommand(Command.Command2(Student("Oneqiong")))
        self.assertEqual(invoker.action(),
                         "Command2 been executed on Oneqiong")

    def test_commands(self):
        student = Student("Gordon")
        c1 = Command.Command1(student)
        c2 = Command.Command2(student)
        c3 = Command.Command3(student)

        invoker = Command.InvokerCommands(c1)
        invoker.addCommand(c3)
        invoker.addCommand(c2)

        ret = invoker.action()
        self.assertEqual(len(ret), 3)

        self.assertEqual(
            ret[0], "Command1 been executed on "+student.getName())
        self.assertEqual(
            ret[1], "Command3 been executed on "+student.getName())
        self.assertEqual(
            ret[2], "Command2 been executed on "+student.getName())
