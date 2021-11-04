from random import randint


class Card(object):
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]  # Clubs < Diamonds < Hearts < Spades
    rank_names = [None, "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                  "King"]

    def __init__(self, suit=None, rank=None):
        if suit is None and rank is None:
            self.suit = randint(0, 3)  # random suit
            self.rank = randint(1, 13)  # random rank
        else:
            self.suit = suit
            self.rank = rank

    def __str__(self):
        return self.suit_names[self.suit] + " " + self.rank_names[self.rank]

    def __lt__(self, other):
        if self.suit > other.suit:
            return True
        if self.suit < other.suit:
            return False
        if self.rank > other.rank:
            return True
        if self.rank < other.rank:
            return False

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    # def __ne__(self, other):
    #     print("ne ...")
    #     return not (self.suit == other.suit and self.rank == other.rank)
    def rate_a_card(self):
        return int("{}{}".format(self.rank, self.suit))
# card = Card(2, 11)
# print(card)
print("hi")