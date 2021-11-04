from deck import Deck


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.rate = 0

    def hand_rate(self):
        for c in self.cards:
            self.rate += c.rate_a_card()
        return self.rate

    def compare_hands(self, other):
        if self.hand_rate() > other.hand_rate():
            print("{} wins!".format(self.label))
        elif self.hand_rate() < other.hand_rate():
            print("{} wins!".format(other.label))
        else:
            print("no winner ...")

    def add_card(self, card):
        self.add_card(card)
        self.rate += card.rate_a_card()


hand = Hand("my hand")
deck = Deck()
for k in range(13):
    hand.add_card(deck.pop_card())
# print(hand.cards)
# print(hand.label)
print(hand)
# hand.sort()
# print(hand)
