from unittest import TestCase

from domain import User, Cast, Auction


class TestAuction(TestCase):
    def setUp(self) -> None:
        self.gui = User("Guilherme")

        self.gui_cast = Cast(self.gui, 150.0)

        self.auction = Auction("Cellphone")

    def test_auction(self):
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

    def test_allow_cast_in_empty_auction(self):
        self.auction.add_cast(self.gui_cast)

        self.assertEqual(1, len(self.auction.casts))

    def test_allow_cast_if_last_user_is_different(self):
        yuri = User("Yuri")
        yuri_cast = Cast(yuri, 200.0)

        self.auction.add_cast(yuri_cast)
        self.auction.add_cast(self.gui_cast)

        self.assertEqual(2, len(self.auction.casts))

    def test_not_allow_cast_if_last_user_is_the_same(self):
        gui_cast200 = Cast(self.gui, 200.0)

        self.auction.add_cast(self.gui_cast)
        self.auction.add_cast(gui_cast200)

        self.assertEqual(1, len(self.auction.casts))
