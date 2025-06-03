import unittest

from Behavioural import Mediator


class MediatorTest(unittest.TestCase):
    def test_mediator(self):
        center = Mediator.Mediator()

        gordon = Mediator.Colleague(center, "Gordon")
        oneqiong = Mediator.Colleague(center, "Oneqiong")
        center.register(gordon)
        center.register(oneqiong)

        center.buyOffer("NTES", 19, oneqiong.colleagueId)
        center.sellOffer("NTES", 19, gordon.colleagueId)

        self.assertEqual(len(center.colleagues), 2)
        self.assertEqual(center.lastId, 2)
        self.assertEqual(len(center.buyOffers), 0)
        self.assertEqual(len(center.sellOffers), 0)

        center.sellOffer("TSLA", 190, oneqiong.colleagueId)
        self.assertEqual(len(center.buyOffers), 0)
        self.assertEqual(len(center.sellOffers), 1)
