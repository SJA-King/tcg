# TODO maybe make all these methods in a class

# TODO Note that piles have to be a list of card objects

# from .gen1.attacks import ATTACKS
# from .gen1.pokepowers import POKEPOWERS
from dataclasses import dataclass, field
from attacks import Attacks
from common import Types
from pokepowers import PokePower


def play_card(card_name: str) -> None:
    globals()[card_name]()


# TODO in GAME.py have a lookup of "str" to thing

@dataclass
class Card:
    _name: str = ""
    _description: str = ""
    _hit_points: int = 0

    @property
    def name(self):
        return self.name

    @property
    def description(self):
        return self._description

    @property
    def hit_points(self):
        return self._hit_points


@dataclass
class Pokemon(Card):
    _type: Types = None
    _attacks: list[str] = None
    _resistance: Types = None
    _weakness: Types = None
    _retreat_cost: int = None
    _pokepower: PokePower = None
    _evolution_stage: str = ""  # TODO think about this one

    @property
    def type(self):
        return self._type

    @property
    def attacks(self):
        return self._attacks

    # @property
    # def attack_two_name(self):
    #     return self._attack_two_name
    #
    # @property
    # def attack_three_name(self):
    #     return self._attack_three_name

    @property
    def resistance(self):
        return self._resistance

    @property
    def weakness(self):
        return self._weakness

    @property
    def retreat_cost(self):
        return self._retreat_cost

    @property
    def pokepower(self):
        return self._pokepower

    @property
    def evolution_stage(self):
        return self._evolution_stage



# TODO below to change things to enums maybe
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

