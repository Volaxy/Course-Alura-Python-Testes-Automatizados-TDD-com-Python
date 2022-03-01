from tests.exceptions import InvalidCast


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
        if value <= self.__wallet:
            cast = Cast(self, value)
            auction.add_cast(cast)

            self.__wallet -= value
        else:
            raise InvalidCast("Do not propose a cast with the value greater than the wallet value")


class Cast:
    def __init__(self, user, value):
        self.user = user
        self.value = value


class Auction:
    def __init__(self, description):
        self.description = description
        self.__casts = []

        self.lowest_bidder = 0.0
        self.highest_bidder = 0.0

    def add_cast(self, cast: Cast):
        if not self.__casts or self.__casts[-1].user != cast.user and cast.value > self.__casts[-1].value:
            if not self.__casts:
                self.lowest_bidder = cast.value

            self.highest_bidder = cast.value

            self.__casts.append(cast)
        else:
            raise InvalidCast("The same user do not propose two casts in a row")

    @property
    def casts(self):
        return self.__casts[:]
