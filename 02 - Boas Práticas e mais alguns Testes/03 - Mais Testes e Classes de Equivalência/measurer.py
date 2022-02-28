import sys

from domain import Auction


class Measurer:
    def __init__(self):
        self.lowest_bidder = sys.float_info.max
        self.highest_bidder = sys.float_info.min

    def evaluate(self, auction: Auction):
        for cast in auction.casts:
            if cast.value < self.lowest_bidder:
                self.lowest_bidder = cast.value
            if cast.value > self.highest_bidder:
                self.highest_bidder = cast.value
