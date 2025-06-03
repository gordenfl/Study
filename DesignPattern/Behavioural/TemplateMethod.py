class Pizza(object):
    PIZZA_SIZE = {
        "SMALL": 0,
        "MEDIA": 1,
        "LARGE": 2,
    }
    PIZZA_TYPE = {
        "MEAT": 0,
        "CHEESE": 1,
        "FULL": 2,
    }

    def __init__(self, size):
        self.meat = False
        self.cheese = False
        self.pizzaType = None
        self.size = -1
        self.cooked = False

    def cookPizza(self):
        self.cooked = True

    def addMeat(self):
        pass

    def addCheese(self):
        pass

    def getMeat(self):
        return self.meat

    def getCheese(self):
        return self.cheese

    def getPrice(self):
        return 0


class CheesePizza(Pizza):
    def __init__(self, size):
        super(CheesePizza, self).__init__(size)
        self.pizzaType = Pizza.PIZZA_TYPE["CHEESE"]

    def getPrice(self):
        return 10

    def addCheese(self):
        self.cheese = True
        return


class MeatPizza(Pizza):
    def __init__(self, size):
        super(MeatPizza, self).__init__(size)
        self.pizzaType = Pizza.PIZZA_TYPE["MEAT"]

    def getPrice(self):
        return 15

    def addMeat(self):
        self.meat = True


class FullPizza(Pizza):
    def __init__(self, size):
        super(FullPizza, self).__init__(size)
        self.pizzaType = Pizza.PIZZA_TYPE["FULL"]

    def addMeat(self):
        self.meat = True

    def addCheese(self):
        self.cheese = True

    def getPrice(self):
        return 25


class BasePizzaStore(object):
    def __init__(self):
        self.pizza = None

    def MakePizza(self, pType, pSize, address):
        price = self.TakeOrder(pType, pSize)

        if -1 == price:
            return None
        if not self.ProcessPayment(price):
            return None

        if not self.BuildPizza():
            return None

        if not self.CookPizza():
            return None
        if not self.DeliverPizza(address):
            return None
        return self.pizza

    def TakeOrder(self, pType, pSize):
        pass

    def BuildPizza(self):
        pass

    def CookPizza(self):
        pass

    def DeliverPizza(self, address):
        #print("Deliver to:"+address)
        return True

    def ProcessPayment(self, price):
        return True


class DominoPizzaStore(BasePizzaStore):
    def __init__(self):
        super(DominoPizzaStore, self).__init__()

    def TakeOrder(self, pType, pSize):
        if pType == Pizza.PIZZA_TYPE["CHEESE"]:
            self.pizza = CheesePizza(pSize)
            return self.pizza.getPrice()
        if pType == Pizza.PIZZA_TYPE["MEAT"]:
            self.pizza = MeatPizza(pSize)
            return self.pizza.getPrice()
        if pType == Pizza.PIZZA_TYPE["FULL"]:
            self.pizza = FullPizza(pSize)
            return self.pizza.getPrice()

        return -1

    def BuildPizza(self):
        self.pizza.addCheese()
        self.pizza.addMeat()
        return True

    def CookPizza(self):
        self.pizza.cookPizza()
        return True
