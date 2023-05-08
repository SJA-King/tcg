from .cards import Card

import random


class Pile:

    def __init__(self, card_list: list[Card]):
        # self._name = name
        self._cards = card_list

    @property
    def cards(self):
        return self._cards

    def cards_left(self):
        return len(self._cards)


class Deck(Pile):
    """ Initalised with 60 cards """
    # def __init__(self, card_list):
    #     super().__init__("Deck", card_list)

    def shuffle(self):
        random.shuffle(self._cards)


class Hand(Pile):
    """ Hand is created on Turn 0 and given 7 cards """
    pass
    # def __init__(self, card_list):
    #     super().__init__("Hand", card_list)
        # TODO check theres a basic pokemon
        # TODO offer a mulligan

    # @property
    # def cards(self):
    #     return self._cards


class Discard(Pile):
    pass

    # def __init__(self, card_list):
    #     super().__init__("Discard", card_list)

    # @property
    # def cards(self):
    #     return self._cards


class Prizes(Pile):
    pass

    # def __init__(self, card_list):
    #     super().__init__("Prizes", card_list)
    #     self._drawn: bool = False  # TODO may not need this

    # def lock(self):  # TODO may not need this
    #     self._drawn = True  # TODO may not need this
