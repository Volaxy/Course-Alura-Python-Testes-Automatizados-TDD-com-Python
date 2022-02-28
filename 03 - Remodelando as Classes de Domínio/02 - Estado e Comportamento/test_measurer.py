from unittest import TestCase

from domain import User, Cast, Auction


class TestMeasurer(TestCase):
    def setUp(self) -> None:
        self.gui = User("Guilherme")

        self.gui_cast = Cast(self.gui, 150.0)

        self.auction = Auction("Cellphone")

    def test_measurer(self):
        yuri = User("Yuri")

        yuri_cast = Cast(yuri, 100.0)

        self.auction.add_cast(self.gui_cast)
        self.auction.add_cast(yuri_cast)

        for cast in self.auction.casts:
            print(f"The user {cast.user.name} made a bid of {cast.value}")

        self.assertEqual(100.0, self.auction.lowest_bidder)
        self.assertEqual(150.0, self.auction.highest_bidder)

    def test_one_cast(self):
        self.auction.add_cast(self.gui_cast)

        for cast in self.auction.casts:
            print(f"The user {cast.user.name} made a bid of {cast.value}")

        self.assertEqual(150.0, self.auction.lowest_bidder)
        self.assertEqual(150.0, self.auction.highest_bidder)
