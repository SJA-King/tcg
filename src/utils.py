import os
from pathlib import Path
from typing import Union
from yaml import safe_load

from .cards import Card
from .common import GenerationSubSets, SETS_PATH


def check_file_path(file_path: str) -> str:
    """ Check a file exists """
    assert os.path.exists(file_path), f"{file_path} not found!"
    print(f"Found: {file_path}")
    return file_path


def get_yml_data(yml_path: Union[str, Path]) -> dict:
    """ import yml data from a yml file """
    check_file_path(yml_path)
    with open(yml_path, 'r') as stream:
        yml_data = safe_load(stream)
    return yml_data


def import_deck_list(deck_filepath: Union[str, Path]) -> dict:
    return get_yml_data(deck_filepath)


def import_card_list_yml(card_list_filepath: Union[str, Path]) -> dict:
    return get_yml_data(card_list_filepath)


# def import_gen_card_list(generation: GenerationSets = GenerationSets.gen1) -> dict:
def import_gen_card_list(generation: str = "gen1") -> dict:
    cards_in_gen = {}
    for i_card_list in GenerationSubSets[generation].value:
        card_list_path = SETS_PATH / generation / f"{i_card_list}.yml"
        sub_gen_card_list = import_card_list_yml(card_list_path)
        cards_in_gen.update(sub_gen_card_list)

    return cards_in_gen

# todo maybe should just have them defined in source and not in yml as there is no real need to have cards in yml as i import them anyway
# TODO a DECK can be in yml though as thats just a "dict/list"!!!


# def import_set(generations: GenerationSets = GenerationSets.gen1, subset: GenerationSubSets = None):
#     raise NotImplementedError
#
#
#
# def make_deck(generations: GenerationSets = GenerationSets.gen1,
#               deck_name: str = None,
#               available_cards: list[Card] = None) -> list[Card]:
#     raise NotImplementedError