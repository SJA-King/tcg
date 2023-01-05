# TODO maybe make all these methods in a class

# TODO Note that piles have to be a list of card objects

from attacks import ATTACKS
from pokepowers import POKEPOWERS


class Card:
    in_play = False

    def __init__(self, name, description):
        self.name = name
        # TODO is an "effect" a generic for an action, command etc. E.g. an attack or a pokepower is an effect, like a trainer's effect?
        self.description = description


class Pokemon(Card):

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
        self.stage = attributes["stage"]


class Trainer(Card):
    pass


# class Supporter(Trainer):

class Energy(Card):

    def __init__(self, name: str = "Energy", amount: int = 1, basic: bool = True):
        super().__init__(name, "")
        self.amount = amount
        self.basic = basic


ENERGIES = {
    "Psychic": Energy("Psychic"),
    "Lightning": Energy("Lightning"),
    "Fire": Energy("Fire"),
    "Water": Energy("Water"),
    "Grass": Energy("Grass"),
    "Fighting": Energy("Fighting"),
    "Double Colorless": Energy("Double Colorless", amount=2, basic=False),
}


# class Stadium(Trainer):
#     pass


