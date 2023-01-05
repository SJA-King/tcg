# This is the game!
import pathlib

from player import Player
from common import get_yml_data, SETS_PATH, SETS
from cards import ENERGIES

DECKS = {
    "haymaker": None
}


class Game:

    def __init__(self, one: Player = None, two: Player = None):
        self.player_1 = one
        self.player_2 = two


def get_card_sets_pokemon(generation: str, card_set: str, card_type: str) -> dict:
    path = SETS_PATH / generation / card_set / f"{card_type}.yml"
    return get_yml_data(path)


def get_generations_pokemon(generation: str) -> dict:
    generations_pokemon = {}
    for card_set in SETS[generation]:
        generations_pokemon.update(get_card_sets_pokemon(generation, card_set, "pokemon"))

    return generations_pokemon


def make_card_list():
    # TODO get all pokemon from generation
    # TODO get all trainers from generation

    # TODO make list of pokemon objects
    # TODO make list of trainer objects
    pass


def add_pokemon() -> list:
    pass


def add_trainers() -> list:
    pass


def add_energies() -> list:
    pass


def make_deck(deck_yml: pathlib.Path = None) -> list:
    deck_list = get_yml_data(deck_yml)

    deck = []
    deck += add_pokemon(deck_list["Pokemon"])
    deck += add_trainers(deck_list["Trainers"])
    deck += add_energies(deck_list["Energies"])

    return deck



def make_decks(generation: str = None) -> None:

    for deck_name in DECKS.keys():
        deck_path = pathlib.Path("")
        deck = make_deck(deck_path)
        DECKS[deck_name] = deck


def pick_deck():
    pass




make_card_list()
make_decks()

Game(Player("One"), Player("Two"))


