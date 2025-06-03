# Support a very large number of fine-grained objects
# Requirement: the state information of each object can be retrieved on demand

class BaseImage(object):
    def __init__(self, filename=None):
        self.filename = filename

    def Display(self, x, y, width, height):
        pass


class Image(BaseImage):
    def __init__(self, filename):
        super().__init__(filename=filename)

    def Display(self, x, y, width, height):
        return "<img src='%s' style=\"left:%d; top:%d; width:%d; height%d;\" />" % (self.filename, x, y, width, height)


class ImageFactory(object):
    def __init__(self):
        self.flyweights = {}

    def getFlyweight(self, filename):
        if filename not in self.flyweights:
            newobj = Image(filename)
            self.flyweights[filename] = newobj

        return self.flyweights[filename]
    
    def getSize(self):
        return len(self.flyweights)
