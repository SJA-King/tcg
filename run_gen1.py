from src.game import Game
from src.player import Player
from src.cards import Card

from typing import final

MAX_TURNS: final(int) = 999

player_one = Player("Bethany")
player_two = Player("Simon")

this_game = Game(one=player_one, two=player_two, generation=1)

player_two.deck = [Card(name="A"), Card(name="B"), Card(name="C"), Card(name="D")]
player_one.deck = [Card(name="E"), Card(name="F")]

while this_game.total_turns < MAX_TURNS:

    this_game.swap_player()
    # TODO Put below print as logging in swap_player
    print(f"Turn: {this_game.total_turns}, Player: {this_game.player_turn()} ")

    if not this_game.turn_draw_card():
        print(f"Player '{this_game.current_player.name}' has no cards in deck! '{this_game.other_player.name}' Wins!")
        break

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