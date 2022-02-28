import sys


class User:
    def __init__(self, name, wallet):
        self.__name = name
        self.__wallet = wallet

    @property
    def name(self):
        return self.__name

    @property
    def wallet(self):
        return self.__wallet

    def propose_bid(self, auction, value):
        cast = Cast(self, value)
        auction.add_cast(cast)

        self.__wallet -= value


class Cast:
    def __init__(self, user, value):
        self.user = user
        self.value = value


class Auction:
    def __init__(self, description):
        self.description = description
        self.__casts = []

        self.lowest_bidder = sys.float_info.max
        self.highest_bidder = sys.float_info.min

    def add_cast(self, cast: Cast):
        if not self.__casts or self.__casts[-1].user != cast.user and cast.value > self.__casts[-1].value:
            if cast.value < self.lowest_bidder:
                self.lowest_bidder = cast.value
            if cast.value > self.highest_bidder:
                self.highest_bidder = cast.value

            self.__casts.append(cast)
        else:
            raise ValueError("The same user do not propose two casts in a row")

    @property
    def casts(self):
        return self.__casts[:]
