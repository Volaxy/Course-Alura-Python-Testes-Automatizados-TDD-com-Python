from domain import User, Cast, Auction
from measurer import Measurer


def __main__():
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

    print(f"The lower bidder was {measurer.lowest_bidder} and the highest bidder was {measurer.highest_bidder}")


if __name__ == "__main__":
    __main__()
