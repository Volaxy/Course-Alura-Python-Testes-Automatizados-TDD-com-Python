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

    def add_cast(self, cast: Cast):
        self.__casts.append(cast)

    @property
    def casts(self):
        # The "[:]" return a copy of the list
        return self.__casts[:]
