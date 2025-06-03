import unittest
from Behavioural import Iterator


class IteratorTest(unittest.TestCase):
    def test_createIterator(self):
        songs = Iterator.SongsOf2000()
        songs.addSong("Song1", "S1", 2000)
        songs.addSong("Song2", "S1", 2000)
        songs.addSong("Song3", "S1", 2000)
        songs.addSong("Song11", "S2", 2000)
        songs.addSong("Song12", "S2", 2000)
        songs.addSong("Song13", "S2", 2000)
        self.assertEqual(songs.getSongs(), "%s %s %d" % ("Song1", "S1", 2000))
        self.assertEqual(songs.getSongs(), "%s %s %d" % ("Song2", "S1", 2000))
        self.assertEqual(songs.getSongs(), "%s %s %d" % ("Song3", "S1", 2000))
        self.assertEqual(songs.getSongs(), "%s %s %d" % ("Song11", "S2", 2000))
        self.assertEqual(songs.getSongs(), "%s %s %d" % ("Song12", "S2", 2000))
        self.assertEqual(songs.getSongs(), "%s %s %d" % ("Song13", "S2", 2000))
        self.assertEqual(songs.getSongs(), "End")

        songs = Iterator.SongsOf1999()
        songs.addSong("Song1", "S1", 1999)
        songs.addSong("Song2", "S1", 1999)
        songs.addSong("Song3", "S1", 1999)
        songs.addSong("Song11", "S2", 1999)
        songs.addSong("Song12", "S2", 1999)

        self.assertEqual(songs.getSongs(), "%s %s %d" % ("Song1", "S1", 1999))
        self.assertEqual(songs.getSongs(), "%s %s %d" % ("Song2", "S1", 1999))
        self.assertEqual(songs.getSongs(), "%s %s %d" % ("Song3", "S1", 1999))
        self.assertEqual(songs.getSongs(), "%s %s %d" % ("Song11", "S2", 1999))
        self.assertEqual(songs.getSongs(), "%s %s %d" % ("Song12", "S2", 1999))
        self.assertEqual(songs.getSongs(), "End")
