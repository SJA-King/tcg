from .src.game import Game
from .src.player import Player

player_one = Player()
player_two = Player()

this_game = Game(player_one=player_one, player_two=player_two)

this_game.import_cardset(generation=1)
this_game.import_all_decks(generation=1)
player_one.assign_deck("Haymaker")
player_two.assign_deck("buzzzapdos")

this_game.list_cards(generation=1)
this_game.list_cards(generation=1, flavour="trainers")
this_game.list_cards_pokemon(generation=1)

this_game.list_attacks(generation=1)
this_game.list_pokepowers(generation=1)

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