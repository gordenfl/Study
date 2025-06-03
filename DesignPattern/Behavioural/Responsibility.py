class Numbers(object):
    def __init__(self, num1, num2, action):
        self.num1, self.num2 = num1, num2  # two number of action need
        self.action = action  # string of symbol of action such like + - * /

    def getNum1(self):
        return self.num1

    def getNum2(self):
        return self.num2

    def getAction(self):
        return self.action


class Chain(object):
    def __init__(self):
        self.next = None

    def setNext(self, chain):
        self.next = chain

    def do(self, val):  # val is a type of Numbers
        pass


class AddNumber(Chain):
    def do(self, val):  # val is a type of Numbers
        if val.getAction() == "+":
            return "%d+%d=%d" % (val.getNum1(), val.getNum2(), val.getNum1()+val.getNum2())
        else:
            if not self.next:
                return "we can not deal with action of "+val.getAction()

            return self.next.do(val)


class SubNumber(Chain):
    def do(self, val):
        if val.getAction() == "-":
            return "%d-%d=%d" % (val.getNum1(), val.getNum2(), val.getNum1()-val.getNum2())
        else:
            if not self.next:
                return "we can not deal with action of "+val.getAction()

            return self.next.do(val)


class MulNumber(Chain):
    def do(self, val):
        if val.getAction() == "*":
            return "%d*%d=%d" % (val.getNum1(), val.getNum2(), val.getNum1()*val.getNum2())
        else:
            if not self.next:
                return "we can not deal with action of "+val.getAction()

            return self.next.do(val)


class DivNumber(Chain):
    def do(self, val):
        if val.getAction() == "/":
            return "%d/%d=%d" % (val.getNum1(), val.getNum2(), val.getNum1()/val.getNum2())
        else:
            if not self.next:
                return "we can not deal with action of "+val.getAction()

            self.next.do(val)
