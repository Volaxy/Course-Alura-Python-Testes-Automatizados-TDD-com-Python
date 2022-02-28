from domain import User, Auction


def test_subtract_value_from_wallet_when_user_proposes_a_bid():
    vini = User("Vini", 100)

    auction = Auction("Cellphone")

    vini.propose_bid(auction, 50.0)

    assert vini.wallet == 50.0
