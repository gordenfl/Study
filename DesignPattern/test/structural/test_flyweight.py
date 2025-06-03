import unittest
from Structural import Flyweight


class TestFlyweight(unittest.TestCase):
    def test_flyweight(self):
        image_factory = Flyweight.ImageFactory()
        img = image_factory.getFlyweight("test.jpg")
        self.assertEqual(img.Display(
            1, 1, 100, 100), "<img src='%s' style=\"left:%d; top:%d; width:%d; height%d;\" />" % ("test.jpg", 1, 1, 100, 100))

        img = image_factory.getFlyweight("test.jpg")
        self.assertEqual(img.Display(
            2, 1, 200, 230), "<img src='%s' style=\"left:%d; top:%d; width:%d; height%d;\" />" % ("test.jpg", 2, 1, 200, 230))

        img = image_factory.getFlyweight("test1.jpg")
        self.assertEqual(img.Display(
            2, 1, 200, 230), "<img src='%s' style=\"left:%d; top:%d; width:%d; height%d;\" />" % ("test1.jpg", 2, 1, 200, 230))

        self.assertEqual(image_factory.getSize(), 2)  # test.jpg test1.jpg
