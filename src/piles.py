# TODO Remove? Maybe not needed


class Pile:

    def __init__(self, name, card_list, viewable=False):
        self.name = name
        self.cards = card_list
        self.viewable = viewable


class Deck(Pile):
    """ Initalised with 60 cards """
    def __init__(self, card_list):
        super().__init__("Deck", card_list)


class Hand(Pile):
    """ Hand is created on Turn 0 and given 7 cards """
    def __init__(self, card_list):
        super().__init__("Hand", card_list, viewable=True)
        # TODO check theres a basic pokemon
        # TODO offer a mulligan


class Discard(Pile):

    def __init__(self, card_list):
        super().__init__("Discard", card_list, viewable=True)
