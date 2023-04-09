from src.game import Game
from src.player import Player

from typing import final

MAX_TURNS: final(int) = 100

print("hello")

player_one = Player("Bethany")
player_two = Player("Simon")

this_game = Game(one=player_one, two=player_two, generation=1)

# Import the cards for this_game to use

# Set decklist for player 1
# Set decklist for player 2

while this_game.total_turns < MAX_TURNS:
    print(f"TURN: {this_game.total_turns}")
    print(this_game.player_turn())
    this_game.swap_player()
    this_game.current_player.draw_card()

    # Wait for action!

    # TODO the rest!


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