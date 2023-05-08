# TODO maybe make all these methods in a class

# TODO Note that piles have to be a list of card objects

# from .gen1.attacks import ATTACKS
# from .gen1.pokepowers import POKEPOWERS
from dataclasses import dataclass, field


def play_card(card_name: str) -> None:
    globals()[card_name]()


# TODO in GAME.py have a lookup of "str" to thing

@dataclass
class Card:
    name: str = ""
    description: str = ""
    hit_points: int = 0


@dataclass
class Pokemon(Card):
    type: str = ""
    # TODO theres only max 3 attacks so maybe easier to have individual
    attacks: list[str] = field(default_factory=list)
    resistance: str = ""
    weakness: str = ""
    retreat_cost: str = ""
    pokepower: str = ""
    evolution_stage: str = ""


    # def __init__(self, pokemon_name: str = "Pokemon", pokemon_attributes: dict = None):
    #     super().__init__(pokemon_name, "")
    #     self.type = None
    #     self.hp = None
    #     self.set_attributes(pokemon_attributes)
    #
    # def set_attributes(self, attributes: dict = None):
    #     if not attributes:
    #         raise Exception(f"{self.name} has empty attributes!")
    #     self.hp = attributes["hp"]
    #     self.type = attributes["type"]
    #     self.attack_1 = ATTACKS[attributes["attack_1"]]
    #     self.attack_2 = ATTACKS[attributes["attack_2"]]
    #     self.resistance = attributes["resistance"]
    #     self.weakness = attributes["weakness"]
    #     self.retreat_cost = attributes["retreat_cost"]
    #     self.pokepower = POKEPOWERS[attributes["pokepower"]]
    #     self.stage = attributes["stage"]

@dataclass
class Trainer(Card):
    #if so we could just have 'move' rather than 'draw' and / or 'discard'
    discard: int = 0
    draw: int = 0
    move: int = 0
    # NEED draw, discard and move, to make things easier!
    heal: bool = False
    switch: bool = False  # Used to swap active and bench OR active to hand
    player: str = ""
    # TODO need a position_from and a _to -- a to b?
    position_from: str = ""
    position_to: str = ""
    # position on its own is singular space? or should it always be a->b?
    position: str = ""  # E.g. hand, active, bench, deck, discard_pile
    attach: bool = False
    card_type: str = ""  # e.g. 'energy', 'trainer'
    # TODO need a select? rather than automatic?


# class Supporter(Trainer):
# TODO

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
# TODO

