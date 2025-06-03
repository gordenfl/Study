from abc import ABC, ABCMeta, abstractmethod


class SongInfo(object):
    def __init__(self, name, band, year):
        self.name = name
        self.band = band
        self.year = year

    def getName(self):
        return self.name

    def getBand(self):
        return self.band

    def getYear(self):
        return self.year

    def getInfo(self):
        return "%s %s %d" % (self.name, self.band, self.year)


class Iterator(metaclass=ABCMeta):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def remove(self):
        pass


class ArrayIterator(Iterator):
    def __init__(self, data):
        super().__init__(data)
        self.current = 0

    def next(self):
        val = self.data[self.current]
        self.current += 1
        return val

    def hasNext(self):
        return self.current < len(self.data)

    def remove(self):
        self.data.remove(self.data[self.current])


class DictionaryIterator(Iterator):
    def __init__(self, data):
        super().__init__(data)
        self.current = 0

    def next(self):
        keys = list(self.data.keys())
        val = self.data[keys[self.current]]
        self.current += 1
        return val

    def hasNext(self):
        return self.current < len(self.data.keys())

    def remove(self):
        keys = self.data.keys()
        del self.data[keys[self.current]]


class SongsOf1999(object):
    def __init__(self):
        self.songs = {}
        self.iterator = DictionaryIterator(self.songs)

    def addSong(self, name, band, year):
        self.songs[name] = SongInfo(name, band, year)

    def getSongs(self):
        if self.iterator.hasNext():
            return self.iterator.next().getInfo()
        return "End"


class SongsOf2000(object):
    def __init__(self):
        self.songs = []
        self.iterator = ArrayIterator(self.songs)

    def addSong(self, name, band, year):
        self.songs.append(SongInfo(name, band, year))

    def getSongs(self):
        if self.iterator.hasNext():
            return self.iterator.next().getInfo()
        else:
            return "End"
