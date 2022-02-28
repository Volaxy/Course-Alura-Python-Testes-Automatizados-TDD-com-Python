from domain import User, Auction


def test_subtract_value_from_wallet_when_user_proposes_a_bid():
    vini = User("Vini", 100)

    auction = Auction("Cellphone")

    vini.propose_bid(auction, 50.0)

    assert vini.wallet == 50.0


def test_allow_cast_when_value_is_less_than_wallet_value():
    vini = User("Vini", 100)

    auction = Auction("Cellphone")

    vini.propose_bid(auction, 1.0)

    assert vini.wallet == 99.0


def test_allow_cast_when_value_is_equal_to_wallet_value():
    vini = User("Vini", 100)

    auction = Auction("Cellphone")

    vini.propose_bid(auction, 100.0)

    assert vini.wallet == 0.0


def test_do_not_allow_cast_when_value_is_greater_than_the_wallet_value():
    vini = User("Vini", 100)

    auction = Auction("Cellphone")

    vini.propose_bid(auction, 200.0)

    assert vini.wallet == 100.0
