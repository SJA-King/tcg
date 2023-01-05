# Simple testing script
import yaml
import common

import os


def get_yaml(filename: str) -> dict:
    with open(filename) as f:

        return yaml.load(f, Loader=yaml.FullLoader)


# # TODO change to pathlib
# here = os.path.dirname(os.path.abspath(__file__))
# tcg = os.path.dirname(here)
# decks = os.path.join(tcg, "decks")
# decks_gen1 = os.path.join(decks, "gen1")
# haymake_deck = os.path.join(decks_gen1, "base_set", "haymaker.yml")
# print(haymake_deck)
# print(get_yaml(haymake_deck))

print(common.get_generations_pokemon("gen1"))
