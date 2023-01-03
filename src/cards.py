# TODO maybe make all these methods in a class

# TODO Note that piles have to be a list of card objects
def move_card(from_pile: list, to_pile: list) -> [list, list]:
    """ Move a single card from one pile to another """
    # TODO check piles arent empty!
    from_pile.pop()
    to_pile.append(from_pile[0])
    return from_pile, to_pile


def move_cards(from_pile: list, to_pile: list, number: int = 1) -> [list, list]:
    """ Move multiple cards from one pile to another """
    for n in range(number):
        from_pile, to_pile = move_card(from_pile, to_pile)
    return from_pile, to_pile


def draw_card():
    """ Move a card from the DESK pile to the HAND pile"""
    pass


def draw_cards():
    """ Move multiple cards from the DESK pile to the HAND pile"""
    pass


def select_cards(pile_to_select: list, number: int = 1) -> list:
    """ Select a pile of cards from another pile of cards """
    # TODO INCOMPLETE!
    return pile_to_select


def discard_cards(hand_pile: list, discard_pile: list, number: int = 1) -> [list, list]:
    """ Move cards from HAND pile to DISCARD pile"""
    selection_pile = select_cards(hand_pile)
    _, discard_pile = move_cards(selection_pile, discard_pile, number)
    return hand_pile, discard_pile


class Card:
    in_play = False

    def __init__(self, name, effect):
        self.name = name
        # TODO is an "effect" a generic for an action, command etc. E.g. an attack or a pokepower is an effect, like a trainer's effect?
        self.effect = effect


class Pokemon(Card):
    pass


class Trainer(Card):
    pass


# class Supporter(Trainer):

class Energy(Card):
    pass


# class Stadium(Trainer):
#     pass


