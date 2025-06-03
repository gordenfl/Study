class Product(object):
    def doExecute(self):
        return "do Product parent execute"


class ProductA(Product):
    def doExecute(self):
        return "do ProductA execute"


class ProductB(Product):
    def doExecute(self):
        return "do ProductB execute"


class ProductC(Product):
    def doExecute(self):
        return "do productC execute"


class ProductFactory(object):
    def creatorProduct1(self, name):
        if name == "ProductA":
            return ProductA()
        elif name == "ProductB":
            return ProductB()
        elif name == "ProductC":
            return ProductC()
        else:
            return None

    def creatorProduct2(self, name):
        ProductDict = {
            "ProductA": ProductA,
            "ProductB": ProductB,
            "ProductC": ProductC,
            # ...
        }
        if name not in ProductDict:
            return None
        return ProductDict[name]()