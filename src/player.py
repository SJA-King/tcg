# There are two players
# Each Player has a Deck, Hand, Discard
# Each Player has cards in play -> Active, Bench, Prize
from piles import Deck
from actions import move_card


class Player:

    def __init__(self, name):
        self.name = name
        self.deck = None
        self.hand = None
        self.discard = None
        self.prize_pool = None
        # self.opponent = None

    # TODO maybe player just talks to game?
    # def set_opponent(self, opponent: Player):
    #     self.opponent = opponent

    def set_deck(self, cards_in_deck):
        self.deck = Deck(cards_in_deck)

    def draw_cards(self, number: int):
        """ Move an amount of cards from player DESK pile to player HAND pile"""
        if number < 1:
            raise Exception(f"Cards to draw must be greater than 0!")
        for _ in range(number):
            self.draw_card()

    def draw_card(self):
        """ Move a card from the DESK pile to the HAND pile"""
        self.deck, self.hand = move_card(from_pile=self.deck, to_pile=self.hand)

    def draw_starting_hand(self):
        self.draw_cards(5)

    def select_cards(self, pile_to_select_from, number: int = 1):
    #     TODO get player to pick
        return [pile_to_select_from[0]]

    def discard_cards(self, selection: list) -> [list, list]:
        """ Move cards from a SELECTION pile to DISCARD pile"""
        for _ in range(len(selection)):
            selection, self.discard = move_card(from_pile=selection, to_pile=self.discard)

    def discard_deck_cards(self, number: int = 1):
        selected = self.select_cards(self.deck, number)
        self.discard_cards(selected)

    def discard_hand_cards(self, number: int = 1):
        selected = self.select_cards(self.hand, number)
        self.discard_cards(selected)

    def take_prize(self):
        prize = self.select_cards(self.prize_pool, number=1)
        self.hand.append(prize)
