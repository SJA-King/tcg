from src.game import Game
from src.player import Player
from src.cards import Card, Energy, ENERGIES, Trainer, Pokemon
from src.actions import flip_heads, flip_multiple_heads


import logging
from typing import final

logging.basicConfig(level=logging.INFO)

MAX_TURNS: final(int) = 999

player_one = Player("Bethany")
player_two = Player("Simon")

if not flip_heads():
    player_one, player_two = player_two, player_one

this_game = Game(one=player_one, two=player_two, generation=1)

some_trainers = [Trainer(name=i) for i in "qwertyuiopqwertyuiopqwertyuiopqwert"]
# some_pokemon = [Pokemon(name=i) for i in "asdfghjklasdfghjklas"]
some_pokemon = [Pokemon(name=i) for i in "asdfg"]
some_energy = [Energy(name="Electric") for _ in range(20)]

player_two.deck = some_trainers + some_pokemon + some_energy
player_one.deck = some_trainers + some_pokemon + some_energy

player_one.draw_hand()
player_two.draw_hand()

print(player_one.show_hand())
print(player_two.show_hand())

print(player_two.has_pokemon_in_hand())
print(player_one.has_pokemon_in_hand())

# TODO draw starting hands
## TODO no Pokemon, shuffle then redraw, opponent +1 draw (choice!)

# TODO draw prizes when hands are acceptable
player_two.draw_prizes()

# TODO set active pokemon

# TODO

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