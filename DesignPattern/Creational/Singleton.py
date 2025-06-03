class Singleton(object):
    instance = None

    @staticmethod
    def getInstance():
        if not Singleton.instance:
            Singleton.instance = Singleton()
        return Singleton.instance

    def __init__(self):
        self.info = "Singleton create initial function"
