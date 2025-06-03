# 就像要构建一个SQL解释器一样的需求，可以用这种模式
# 它方便让你构建一个语言解释器，让用户更方便利用你提供的 keyword构建需求
from abc import ABC, ABCMeta, abstractmethod


class AbstractExpression(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def interpret(self, context):
        pass


# example this class should represented the expression of:
#  +, -, *, /, (, ) these symbol, it is not ending of a expression
# it depended the another expression of self.interpret
class NonterminalExpression(AbstractExpression):
    def __init__(self, interpret):  # should a type of AbstractExpression object
        self.interpret = interpret

    def interpret(self, context):
        pass

# this class should represented the symbol of number
# 12, 33, 45, 12, it maybe end of the expression or not


class TerminalExpression(AbstractExpression):
    def __init__(self):
        pass

    def interpret(self, context):
        pass

##########################################################################################


class Expression(metaclass=ABCMeta):
    @abstractmethod
    def Interpret(self):
        pass

# terminal expression


class Number(Expression):
    def __init__(self, value):
        self.value = int(value)

    def Interpret(self):
        return self.value

# non terminal expression


class Add(Expression):
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def Interpret(self):
        return self.left.Interpret()+self.right.Interpret()


class Sub(Expression):
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def Interpret(self):
        return self.left.Interpret()-self.right.Interpret()


class Mul(Exception):
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def Interpret(self):
        return self.left.Interpret()*self.right.Interpret()


class Div(Exception):
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def Interpret(self):
        return self.left.Interpret()/self.right.Interpret()


class Evaluator(object):

    def Parse(self, text):
        stack = []
        words = text.split(' ')
        for word in words:
            if word == "+":
                r = stack.pop()
                l = stack.pop()
                stack.append(Add(l, r))
            elif word == "-":
                r = stack.pop()
                l = stack.pop()
                stack.append(Sub(l, r))
            elif word == "*":
                r = stack.pop()
                l = stack.pop()
                stack.append(Mul(l, r))
            elif word == "/":
                r = stack.pop()
                l = stack.pop()
                stack.append(Div(l, r))
            else:
                stack.append(Number(word))
        return stack.pop()
