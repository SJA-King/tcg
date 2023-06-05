from .cards import Card

import random


class Pile:

    def __init__(self, card_list: list[Card], viewable: bool = False):
        # self._name = name
        self.cards = card_list
        self.viewable = viewable

    def cards_left(self):
        return len(self.cards)

    # TODO 05/06/23 keep fixing
    def __add__(self, other):
        if other.cards:
            self.cards += other


class Deck(Pile):
    """ Source of all Cards used through the game. Set to 60 at the beginning of the match """
    def __init__(self, card_list):
        super().__init__(card_list, viewable=False)

    def shuffle(self):
        random.shuffle(self.cards)


class Hand(Pile):
    """ A Players Hand is where they play most of their cards from """

    def __init__(self, card_list):
        super().__init__(card_list, viewable=True)


class Discard(Pile):
    """ When a Card is 'used up' it is put into the Discard Pile """

    def __init__(self, card_list):
        super().__init__(card_list, viewable=True)


class Prizes(Pile):
    """ At the beginning of the Game a Player has six Prize cards they can take for Knocking Out a Pokemon"""
    def __init__(self, card_list):
        # if len(card_list) != 6:
        #     raise Exception(f"Prize Pool must have 6 Cards!")
        # TODO add check at some point!
        super().__init__(card_list, viewable=False)
