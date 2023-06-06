from src.game import Game
from src.player import Player
from src.cards import Card, Energy, ENERGIES, Trainer, Pokemon
from src.actions import flip_heads, flip_multiple_heads, draw_starting_hand, put_all_cards_back_into_deck
from src.piles import Deck
from src.common import EvoStages


import logging
from typing import final

logging.basicConfig(level=logging.INFO)

MAX_TURNS: final(int) = 100

some_trainers = [Trainer(i) for i in "qwertyuiopqwertyuiopqwertyuiopqwert"]
# some_pokemon = [Pokemon(name=i) for i in "asdfghjklasdfghjklas"]
# TODO temp small amount of Pokemon to make things easy to test
# TODO Make check that deck has at least one basic pokemon!
# TODO make a test for that too!
some_pokemon = [Pokemon(i) for i in "123"] + [Pokemon(i, _evolution_stage=EvoStages.STAGE_ONE) for i in "45"]
some_energy = [Energy(name="Electric") for _ in range(20)]

a_deck = some_trainers + some_pokemon + some_energy
b_deck = some_trainers + some_pokemon + some_energy

player_one = Player("Bethany", chosen_deck=Deck(card_list=a_deck))
player_two = Player("Simon", chosen_deck=Deck(card_list=b_deck))

if not flip_heads():
    player_one, player_two = player_two, player_one

this_game = Game(one=player_one, two=player_two, generation=1)

while not player_one.ready or \
        not player_two.ready:

    for player in [player_one, player_two]:
        if player.ready:
            continue

        if player.has_pokemon_in_hand():
            player.is_ready()
            player.draw_prizes()
        else:
            player.redraw_hand()

        print(f"Player: {player.name}, Hand = {player.show_hand()}")

# TODO no Pokemon, shuffle then redraw, opponent +1 draw (choice!)

# Need to import the cards now proper
# TODO set active pokemon

# TODO Add various tests what I already have!

# TODO give selection opportunity!

while this_game.turns < MAX_TURNS:

    # TODO should this be at the end?
    this_game.begin_turn()

    if this_game.active_player.has_empty_deck():
        print(f"Player '{this_game.other_player.name}' Wins!")
        break

    this_game.active_player.draw_card()
    # print(this_game.active_player.hand)
    # if not this_game.turn_draw_card():

    # print(flip_multiple_heads(3))

    # x = "flip_multiple_heads"
    # print(eval(x(3)))

    # Wait for action!

    # TODO the rest!
#
# this_game.player_1.deck = ["a", "b", "c", "d"]
# this_game.player_1.hand = ["e"]
#
# for n in range(4):
#     this_game.player_1.hand.append(this_game.player_1.deck[0])
#     this_game.player_1.deck.pop(0)
#     print(f"P1: \n-- Hand - {this_game.player_1.hand}\n-- Deck - {this_game.player_1.deck}")
#
#
# this_game.player_2.deck = ["q", "p", "r", "s"]





# Below needs to be added
# TODO
# this_game.import_cardset(generation=1)
# this_game.import_all_decks(generation=1)
# player_one.assign_deck("Haymaker")
# player_two.assign_deck("buzzzapdos")
#
# this_game.list_cards(generation=1)
# this_game.list_cards(generation=1, flavour="trainers")
# this_game.list_cards_pokemon(generation=1)
#
# this_game.list_attacks(generation=1)
# this_game.list_pokepowers(generation=1)

# # Rough API
# player_one.action(["Active", attack=1])
#
# # Inside Game
# return Attacks["Slam"]
# # where
# Attacks = {
#     "slam": Attack(damage=20)
#     "confuse ray": Attack(damage=10, status=confusion)
# }