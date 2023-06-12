import random
import pathlib
from enum import Enum, auto
from typing import final

SRC_PATH = pathlib.Path(__file__).parent
TCG_PATH = SRC_PATH.parent
SETS = {
    "gen1": ["base", "jungle", "fossil"]
}
SETS_PATH: final(pathlib.Path) = TCG_PATH / "sets"
DECKS_PATH: final(pathlib.Path) = TCG_PATH / "decks"


class EnergyTypes(Enum):
    LIGHTNING = "LIGHTNING"
    WATER = "WATER"
    FIRE = "FIRE"
    FIGHTING = "FIGHTING"
    PSYCHIC = "PSYCHIC"
    GRASS = "GRASS"
    COLORLESS = "COLORLESS"

    def __str__(self):
        return self.value


class EvoStages(Enum):
    BASIC = auto()
    STAGE_ONE = auto()
    STAGE_TWO = auto()


gen1 = "gen1"
# class GenerationSets(Enum):
#     gen1 = "gen1"
#
#     def __str__(self):
#         return self.value
#
#
# x = GenerationSets


class GenerationSubSets(Enum):
    gen1 = ["base", "fossil", "jungle"]

    def __str__(self):
        return self.value

