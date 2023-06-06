# TODO maybe make all these methods in a class

# TODO Note that piles have to be a list of card objects

# from .gen1.attacks import ATTACKS
# from .gen1.pokepowers import POKEPOWERS
from dataclasses import dataclass, field
from .attacks import Attacks
from .common import EnergyTypes, EvoStages
from .pokepowers import PokePower

from enum import Enum, auto


def play_card(card_name: str) -> None:
    globals()[card_name]()


# TODO in GAME.py have a lookup of "str" to thing

class CardType(Enum):
    POKEMON = auto()
    TRAINER = auto()
    ENERGY = auto()


@dataclass
class Card:
    _name: str = ""
    _description: str = ""
    _hit_points: int = 0
    _energy_type: EnergyTypes = None
    _card_type: CardType = None

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def hit_points(self):
        return self._hit_points

    @property
    def card_type(self):
        return self._card_type

    @property
    def energy_type(self):
        return self._energy_type


@dataclass
class Pokemon(Card):
    _attacks: list[str] = None
    _resistance: EnergyTypes = None
    _weakness: EnergyTypes = None
    _retreat_cost: int = None
    _pokepower: PokePower = None
    _evolution_stage: EvoStages = EvoStages.BASIC
    _card_type = CardType.POKEMON

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
    _card_type = CardType.TRAINER
    # TODO need a select? rather than automatic?


@dataclass
class Energy(Card):
    _card_type = CardType.ENERGY
    # TODO broken from here!!!
    _name = _energy_type.value
    _basic = True
    _amount = 1
    if not _basic:
        # Assume its the double colorless energy
        _amount = 2

    # def __init__(self, basic: bool = True):
    #     super().__init__()
    #     self._name = self._energy_type.value
    #     self._basic = basic
    #     if not self._basic:
    #         # Assume its the double colorless energy
    #         self.amount = 2


class BasicEnergyCards(Enum):
    LIGHTNING = Energy(_energy_type=EnergyTypes.LIGHTNING)
    PSYCHIC = Energy(energy_type=EnergyTypes.PSYCHIC)
    FIRE = Energy(energy_type=EnergyTypes.FIRE)
    WATER = Energy(energy_type=EnergyTypes.WATER)
    GRASS = Energy(energy_type=EnergyTypes.GRASS)
    FIGHTING = Energy(energy_type=EnergyTypes.FIGHTING)


class SpecialEnergyCards(Enum):
    DOUBLECOLORLESS = Energy(energy_type=EnergyTypes.COLORLESS, basic=False)
