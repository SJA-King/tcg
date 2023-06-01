import random
import pathlib
from typing import Union
from yaml import safe_load
from enum import Enum, auto

SRC_PATH = pathlib.Path(__file__).parent
TCG_PATH = SRC_PATH.parent
SETS = {
    "gen1": ["base_set", "jungle", "fossil"]
}
SETS_PATH = TCG_PATH / "sets"
DECKS_PATH = TCG_PATH / "decks"


class Types(Enum):
    ELECTRIC = auto()
    WATER = auto()
    FIRE = auto()
    FIGHTING = auto()
    PSYCHIC = auto()
    GRASS = auto()
    COLORLESS = auto()  # 'Normal'


def check_file_path(file_path: pathlib.Path) -> None:
    """ Check a file exists """
    assert file_path.is_file(), f"{file_path} not found!"
    print(f"Found: {file_path}")


def get_yml_data(yml_path: Union[str, pathlib.Path]) -> dict:
    """ import yml data from a yml file """
    check_file_path(yml_path)
    with open(yml_path, 'r') as stream:
        yml_data = safe_load(stream)
    return yml_data





def make_pokemon():
    pass


# def get_card_sets_trainer():

# TODO as there are only "3" more energys released over all gens - change this to be a constant!
# def get_sets_energy_cards():


def coin_flip(force_flip: int = None) -> bool:
    # TODO revise this to better test it, e.g. force tails, or heads, or put randint in args?
    """ Simple Heads (true) or Tails (False) method"""
    flip = random.randint(0, 1)
    if force_flip:
        flip = force_flip
    if flip == 0:
        return True
    return False


# TODO move these, this isnt the right place for them
def give_sleep():
    pass


def give_confuse():
    pass


def give_paralysis():
    pass

# TODO for future generations
# def give_poison()
#     pass
#
# def give_burn():
#     pass

STATUSES = {
    "sleep": give_sleep(),
    "confuse": give_confuse(),
    "paralysis": give_paralysis()
}
