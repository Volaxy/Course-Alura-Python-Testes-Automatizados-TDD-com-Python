import sys


class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


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
        if not self.__casts or self.__casts[-1].user != cast.user:
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
