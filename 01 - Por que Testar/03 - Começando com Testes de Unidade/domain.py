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

    @property
    def casts(self):
        return self.__casts
