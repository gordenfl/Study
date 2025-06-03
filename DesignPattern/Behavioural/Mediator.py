from abc import ABCMeta, ABC, abstractmethod


class StockOffer(object):
    def __init__(self, symbol=0, shares=0, colleagueCode=""):
        self.shares = shares
        self.symbol = symbol
        self.colleagueCode = colleagueCode

    def getShare(self):
        return self.shares

    def getSymbol(self):
        return self.symbol

    def getColleagueCode(self):
        return self.colleagueCode


class Colleague(metaclass=ABCMeta):
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.colleagueId = -1
        self.name = name

    def saleOffer(self, symbol, shares):
        self.mediator.saleOffer(symbol, shares, self.colleagueId)

    def buyOffer(self, symbol, shares):
        self.mediator.buyOffer(symbol, shares, self.colleagueId)

    def setColleagueId(self, id):
        self.colleagueId = id


class Mediator(metaclass=ABCMeta):
    def __init__(self):
        self.colleagues = []
        self.lastId = 0

        self.buyOffers = []
        self.sellOffers = []

    def register(self, colleague):
        colleague.setColleagueId(self.lastId)
        self.colleagues.append(colleague)
        self.lastId += 1

    def sellOffer(self, symbol, shares, colleagueId):
        target = None
        for offer in self.buyOffers:
            if offer.getSymbol() == symbol and offer.getShare() == shares:
                target = offer
                break

        if target:
            self.buyOffers.remove(target)
            return True

        self.sellOffers.append(StockOffer(symbol, shares, colleagueId))
        return False

    def buyOffer(self, symbol, shares, colleagueId):
        target = None
        for offer in self.sellOffers:
            if offer.getSymbol() == symbol and offer.getShare() == shares:
                target = offer
                break

        if target:
            self.sellOffers.remove(target)
            return True

        self.buyOffers.append(StockOffer(symbol, shares, colleagueId))
        return False
