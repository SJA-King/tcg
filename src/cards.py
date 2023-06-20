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


class CardFlavour(Enum):
    SUPPORTER = auto()
    STADIUM = auto()
    BASIC = auto()
    DOUBLE = auto()
    # TODO combine EvoStages with this
    # Add STAGE_1?
    # Add STAGE_2?


@dataclass
class Card:
    name: str = ""
    description: str = ""
    card_type: CardType = None
    card_flavour: CardFlavour = None


@dataclass
class Energy(Card):
    energy_type: EnergyTypes = None

    def __post_init__(self):
        self.card_type = CardType.ENERGY
        self.amount = 1
        self.name = self.energy_type.value
        if self.card_flavour == CardFlavour.DOUBLE:
            self.amount = 2


class BasicEnergyCards(Enum):
    LIGHTNING = Energy(energy_type=EnergyTypes.LIGHTNING)
    PSYCHIC = Energy(energy_type=EnergyTypes.PSYCHIC)
    FIRE = Energy(energy_type=EnergyTypes.FIRE)
    WATER = Energy(energy_type=EnergyTypes.WATER)
    GRASS = Energy(energy_type=EnergyTypes.GRASS)
    FIGHTING = Energy(energy_type=EnergyTypes.FIGHTING)


class SpecialEnergyCards(Enum):
    DOUBLECOLORLESS = Energy(energy_type=EnergyTypes.COLORLESS,
                             card_flavour=CardFlavour.DOUBLE)

