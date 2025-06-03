# 一个对象在多个状态中转换，同时只能出于其中一种状态中
# 对象的行为随着每个状态转换而发生根本变化

# disadvantages:
'''
The pattern concentrates all code corresponding to a single state into one state class, but spreads out the code of a single context operation over many state classes which can make the code hard to maintain
You need to be very careful that each state has a reachable successor state. It's very common for state machines to hang in a specific state with no way out
'''
from abc import ABC, ABCMeta, abstractmethod

'''
class State(metaclass=ABCMeta):
    @abstractclassmethod
    def Handle(self, context):
        pass


class StateA(State):
    def Handle(self, context):
        print("StateA handle")
        return StateB()


class StateB(State):
    def Handle(self, context):
        print("StateB handle")
        return StateA()


class Context(object):
    def __init__(self):
        self.state = StateA()

    def Request(self):
        self.state = self.state.Handle(self)


def Logic():
    context = Context()
    for i in range(10):
        context.Request()
'''
######################################################################


class State(metaclass=ABCMeta):
    @abstractmethod
    def InsertCoin(self, machine):
        pass

    @abstractmethod
    def EjectCoin(self, machine):
        pass

    @abstractmethod
    def PushButton(self, machine):
        pass

    @abstractmethod
    def DispenseChocolate(self, machine):
        pass

    @abstractmethod
    def AddChocolate(self, machine):
        return False


class NoCoin(State):
    def InsertCoin(self, machine):
        if machine.ProductCount <= 0:
            #print("Sold out")
            machine.state = SoldOut()
            return False

        machine.state = CoinInserted()
        #print("Coin accepted")
        return True

    def EjectCoin(self, machine):
        #print("can not eject coin (there is no coin)")
        return False

    def PushButton(self, machine):
        #print("no coin")
        return False

    def DispenseChocolate(self, machine):
        #print("no coin")
        return False

    def AddChocolate(self, machine):
        return False


class CoinInserted(State):
    def InsertCoin(self, machine):
        return False

    def EjectCoin(self, machine):
        machine.state = NoCoin()
        return True

    def PushButton(self, machine):
        machine.state = Sold()
        return True

    def DispenseChocolate(self, machine):
        return False

    def AddChocolate(self, machine):
        return False


class Sold(State):
    def InsertCoin(self, machine):
        return False

    def EjectCoin(self, machine):
        return False

    def PushButton(self, machine):
        return False

    def DispenseChocolate(self, machine):
        machine.ProductCount -= 1
        #print("please take your chocolate")
        if machine.ProductCount == 0:
            machine.state = SoldOut()
        else:
            machine.state = NoCoin()
        return True

    def AddChocolate(self, machine):
        return False


class SoldOut(State):
    def InsertCoin(self, machine):
        return False  # print("chocolate sold out")

    def EjectCoin(self, machine):
        return False  # print("can not return coin")
        #machine.state = NoCoin()

    def PushButton(self, machine):
        return False  # print("can not push button")

    def DispenseChocolate(self, machine):
        return False

    def AddChocolate(self, machine):
        machine.ProductCount += 10
        machine.state = NoCoin()
        return True

# 糖果机器


class VendingMachine(object):
    def __init__(self):
        self.ProductCount = 10
        self.state = NoCoin()

    def Help(self):
        print("Vending machine commands:")
        print("1: Insert Coin")
        print("2: Eject Coin")
        print("3: Push Button")
        print("4: Quit")
        print("5: Add Chocolate")

    def InsertCoin(self):
        return self.state.InsertCoin(self)

    def EjectCoin(self):
        return self.state.EjectCoin(self)

    def PushButton(self):
        return self.state.PushButton(self)

    def DispenseChocolate(self):
        return self.state.DispenseChocolate(self)

    def AddChocolate(self):
        return self.state.AddChocolate(self)
