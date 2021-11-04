import random

from alaki import DeckParent
from card import Card


class Deck(DeckParent):
    def __init__(self):
        self.n = 52
        self.cards = []
        n = 0
        while n < self.n:
            card = Card()
            if card not in self.cards:
                self.cards.append(card)
                n += 1
        # for suit in range(4):
        #     for rank in range(1, 14):
        #         card = Card(suit, rank)
        #         self.cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def pop_card(self, where=None):
        if where == 'Top':
            c = self.cards.pop(0)
        elif where == 'Bot':
            c = self.cards.pop()
        else:
            k = random.randint(0, self.n - 1)
            c = self.cards.pop(k)
        self.n -= 1
        return c

    def add_card(self, card):
        self.cards.append(card)

    def sort(self):
        self.cards.sort()

    def __str__(self):
        return '\n'.join([item.__str__() for item in self.cards])


# deck = Deck()
# print(deck)
# print("--------------------------------------")
# deck.sort()
# print(deck)
# print("--------------------------------------")
# deck.shuffle_deck()
# print(deck)
