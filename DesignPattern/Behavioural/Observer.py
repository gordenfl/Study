from abc import ABCMeta, abstractmethod, ABC
class Subject(object):
    def __init__(self):
        self.observers = []
    
    def register(self, o):
        pass
    
    def unregister(self, o):
        pass
    
    def notifyObservers(self):
        pass

class StockGrabber(Subject):
    def __init__(self):
        super(StockGrabber, self).__init__()
        self.ibmPrice = None
        self.applePrice = None
        self.googlePrice = None

    def register(self, o):
        self.observers.append(o)
    
    def unregister(self, o):
        self.observers.remove(o) #
    
    def notifyObservers(self):
        for v in self.observers:
            v.update(self.ibmPrice, self.applePrice, self.googlePrice)
    
    def setIBMPrice(self, price):
        self.ibmPrice = price
        self.notifyObservers()
        
    def setApplePrice(self, price):
        self.applePrice = price
        self.notifyObservers()
        
    def setGooglePrice(self, price):
        self.googlePrice = price
        self.notifyObservers()

# Observer Implements blow:
class Observer(object):
    obverserIDTracker=1
    def __init__(self):
        pass
    
    def update(self, ibmPrice, applePrice, googlePrice):
        pass

class StockObserver(Observer):
    def __init__(self, subject):
        super(StockObserver, self).__init__()
        self.ibmPrice = None
        self.applePrice = None
        self.googlePrice = None
        
        self.obverserId = Observer.obverserIDTracker
        Observer.obverserIDTracker+=1
        
        self.stockGrabber = subject
        self.stockGrabber.register(self)
        
    def update(self, ibmPrice, applePrice, googlePrice):
        self.ibmPrice = ibmPrice
        self.applePrice = applePrice
        self.googlePrice = googlePrice
        self.onPriceChanged()
        
    def onPriceChanged(self):
        #print(self.getInfo())
        pass
    
    def getInfo(self):
        return "Observer ID: %d \nIBM Price: %f\nApple Price: %f\nGoogle Price:%f" % (self.obverserId, self.ibmPrice if self.ibmPrice else 0.0, self.applePrice if self.applePrice else 0.0, self.googlePrice if self.googlePrice else 0.0)
