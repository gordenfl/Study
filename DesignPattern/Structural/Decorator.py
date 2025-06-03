# -*- coding: utf-8 -*-

class Pizza(object):
    def __init__(self):
        self.description = "Unknown Pizza"

    def getDescription(self):
        return self.description

    def getCost(self):
        return 0


class PeppyPaneer(Pizza):
    def __init__(self):
        self.description = "Peppy Paneer"

    def getCost(self):
        return 20


class FarmHouse (Pizza):
    def __init__(self):
        self.description = "Farm House"

    def getCost(self):
        return 200


class Margherita(Pizza):
    def __init__(self):
        self.description = "Margherita"

    def getCost(self):
        return 100

########################  Decorator  ############################


class Decorator(Pizza):  # decorator base class
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza


class FreshTomato(Decorator):  # 加新鲜番茄

    def getDescription(self):
        return self.pizza.getDescription()+", Fresh tomato"

    def getCost(self):
        # self.component.doSomething()
        return self.pizza.getCost() + 40


class Barbeque(Decorator):  # 烧烤炉

    def getDescription(self):
        return self.pizza.getDescription()+", Barbeque"

    def getCost(self):
        return self.pizza.getCost() + 30


class Paneer(Decorator):

    def getDescription(self):
        return self.pizza.getDescription()+", Paneer"

    def getCost(self):
        return self.pizza.getCost() + 20


class Onion(Decorator):  # 洋葱

    def getDescription(self):
        return self.pizza.getDescription()+", Onion"

    def getCost(self):
        return self.pizza.getCost() + 10


def TestCase():
    pizza = PeppyPaneer()
    print(pizza.getDescription()+"----"+str(pizza.getCost()))

    pizza = Barbeque(FreshTomato(Onion(FarmHouse())))
    print(pizza.getDescription()+"----"+str(pizza.getCost()))


if __name__ == "__main__":
    TestCase()
