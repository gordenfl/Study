class Visitor(object):
    def visitLiquor(self, item):
        pass

    def visitTobaco(self, item):
        pass

    def visitNecessity(self, item):
        pass


class TaxVisitor(Visitor):
    def visitLiquor(self, item):
        return int(item.getPrice()*1.1)

    def visitTobaco(self, item):
        return int(item.getPrice()*1.3)

    def visitNecessity(self, item):
        return item.getPrice()


class TaxHolidayVisitor(Visitor):
    def visitLiquor(self, item):
        return int(item.getPrice()*1.2)

    def visitTobaco(self, item):
        return int(item.getPrice()*1.5)

    def visitNecessity(self, item):
        return int(item.getPrice()*1.1)


class Vistable(object):
    def __init__(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def accept(self, visitor):
        pass


class Liquor(Vistable):
    def __init__(self, price):
        super(Liquor, self).__init__(price)

    def accept(self, visitor):
        return visitor.visitLiquor(self)


class Tobaco(Vistable):
    def __init__(self, price):
        super(Tobaco, self).__init__(price)

    def accept(self, visitor):
        return visitor.visitTobaco(self)


class Necessity(Vistable):
    def __init__(self, price):
        super(Necessity, self).__init__(price)

    def accept(self, visitor):
        return visitor.visitNecessity(self)
