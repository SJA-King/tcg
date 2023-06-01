
from enum import Enum, auto
# PokePowers build off actions


def damage_swap():
    raise NotImplementedError


class PokePower(Enum):
    DAMAGE_SWAP = damage_swap()

