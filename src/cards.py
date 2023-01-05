# TODO maybe make all these methods in a class

# TODO Note that piles have to be a list of card objects

from attacks import ATTACKS
from pokepowers import POKEPOWERS


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

    def __init__(self, name, description):
        self.name = name
        # TODO is an "effect" a generic for an action, command etc. E.g. an attack or a pokepower is an effect, like a trainer's effect?
        self.description = description


class Pokemon(Card):
    pass

    def __init__(self, pokemon_name: str = "Pokemon", pokemon_attributes: dict = None):
        super().__init__(pokemon_name, "")
        self.set_attributes(pokemon_attributes)

    def set_attributes(self, attributes: dict = None):
        if not attributes:
            raise Exception(f"{self.name} has empty attributes!")
        self.hp = attributes["hp"]
        self.type = attributes["type"]
        self.attack_1 = ATTACKS[attributes["attack_1"]]
        self.attack_2 = ATTACKS[attributes["attack_2"]]
        self.resistance = attributes["resistance"]
        self.weakness = attributes["weakness"]
        self.retreat_cost = attributes["retreat_cost"]
        self.pokepower = POKEPOWERS[attributes["pokepower"]]


class Trainer(Card):
    pass


# class Supporter(Trainer):

class Energy(Card):
    pass


# class Stadium(Trainer):
#     pass


