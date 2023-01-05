# There are two players
# Each Player has a Deck, Hand, Discard
# Each Player has cards in play -> Active, Bench, Prize
from piles import Deck


class Player:

    def __init__(self, name):
        self.name = name
        self.deck = None

    def set_deck(self, cards_in_deck):
        self.deck = Deck(cards_in_deck)
