from domain import User, Auction

import pytest

from tests.exceptions import InvalidCast


@pytest.fixture
def vini():
    return User("Vini", 100)


@pytest.fixture
def auction():
    return Auction("Cellphone")


def test_subtract_value_from_wallet_when_user_proposes_a_bid(vini, auction):
    vini.propose_bid(auction, 50.0)

    assert vini.wallet == 50.0


def test_allow_cast_when_value_is_less_than_wallet_value(vini, auction):
    vini.propose_bid(auction, 1.0)

    assert vini.wallet == 99.0


def test_allow_cast_when_value_is_equal_to_wallet_value(vini, auction):
    vini.propose_bid(auction, 100.0)

    assert vini.wallet == 0.0


def test_do_not_allow_cast_when_value_is_greater_than_the_wallet_value(vini, auction):
    with pytest.raises(InvalidCast):
        vini.propose_bid(auction, 200.0)
