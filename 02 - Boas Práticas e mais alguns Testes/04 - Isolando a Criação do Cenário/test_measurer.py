from unittest import TestCase

from domain import User, Cast, Auction
from measurer import Measurer


class TestMeasurer(TestCase):
    def setUp(self) -> None:
        self.gui = User("Guilherme")

        self.gui_cast = Cast(self.gui, 150.0)

        self.auction = Auction("Cellphone")

    def test_measurer(self):
        yuri = User("Yuri")

        yuri_cast = Cast(yuri, 100.0)

        self.auction.casts.append(self.gui_cast)
        self.auction.casts.append(yuri_cast)

        for cast in self.auction.casts:
            print(f"The user {cast.user.name} made a bid of {cast.value}")

        measurer = Measurer()

        measurer.evaluate(self.auction)

        self.assertEqual(100.0, measurer.lowest_bidder)
        self.assertEqual(150.0, measurer.highest_bidder)

    def test_one_cast(self):
        self.auction.casts.append(self.gui_cast)

        for cast in self.auction.casts:
            print(f"The user {cast.user.name} made a bid of {cast.value}")

        measurer = Measurer()

        measurer.evaluate(self.auction)

        self.assertEqual(150.0, measurer.lowest_bidder)
        self.assertEqual(150.0, measurer.highest_bidder)
