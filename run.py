from deck import Deck
from hand import Hand

deck = Deck()
deck.shuffle_deck()
# gice 10 cards to Bijan
bijan_hand = Hand("Bijan")
for i in range(10):
    bijan_hand.add_card(deck.pop_card())
deck.sort()
print(deck)
print("{} cards remain in deck".format(deck.n))
print("******************************")
print(bijan_hand)

mitra_hand = Hand("Mitra")
for i in range(10):
    if i % 2:
        c = deck.pop_card("Top")
    else:
        c = deck.pop_card("Bot")
    mitra_hand.add_card(c)
print("******************************")
print(mitra_hand)

bijan_hand.compare_hands(mitra_hand)
