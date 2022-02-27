# The "TestCase" contains an essential methods to test the application
from unittest import TestCase

from domain import User, Cast, Auction
from measurer import Measurer


class TestMeasurer(TestCase):
    def test_evaluate(self):
        gui = User("Guilherme")
        yuri = User("Yuri")

        gui_cast = Cast(gui, 150.0)
        yuri_cast = Cast(yuri, 100.0)

        auction = Auction("Cellphone")
        auction.casts.append(gui_cast)
        auction.casts.append(yuri_cast)

        for cast in auction.casts:
            print(f"The user {cast.user.name} made a bid of {cast.value}")

        measurer = Measurer()

        measurer.evaluate(auction)

        # The method "assertEqual" verify if the second parameter is equal to the first Parameter, in case it's fake,
        # the method, return the actual value of the second parameter
        self.assertEqual(100.0, measurer.lowest_bidder)
        self.assertEqual(150.0, measurer.highest_bidder)
