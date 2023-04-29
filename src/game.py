# This is the game!

from .player import Player
# from common import get_yml_data, SETS_PATH, SETS, DECKS_PATH
# from cards import ENERGIES
from tcg.src.actions import move_cards_between_piles
DECKS = {
    "haymaker": None,
    "buzzapdos": None
}

# TODO have a GameDetails thats a dataclass and a Game(GameDetails)
# game is behavioural

class Game:

    def __init__(self, one: Player, two: Player, generation: int = 0):#, legal_card_sets: [str] = None):
        self.player_1 = one
        # self.player_1.set_opponent(two)
        self.player_2 = two
        # self.player_1.set_opponent(one)
        # TODO set this based on coin flip!
        self.players = [self.player_1, self.player_2]
        self.generation = generation
        # self.legal_cards_sets = legal_card_sets
        self.legal_cards = None
        self.decks_available = None
        self.total_turns = 0
        self.current_player = None
        self.other_player = None

    def begin_turn(self):
        self.swap_player()
        self.total_turns += 1

    def swap_player(self):
        self.players = self.players.reverse()
        # if self.total_turns % 2 == 0:
        #     self.current_player = self.player_1
        #     self.other_player = self.player_2
        # else:
        #     self.current_player = self.player_2
        #     self.other_player = self.player_1
        # self.total_turns += 1

    def get_active_player(self):
        return self.players[0]

    def get_other_player(self):
        return self.players[1]

    # @property
    # def active_player(self):
    #     # if self.current_player:
    #     return self.current_player.name
    #     # return None

    def turn_draw_card(self):
        if self.current_player.deck:
            move_cards_between_piles(from_pile=self.current_player.deck, to_pile=self.current_player.hand)
            return True
        return False

    # def get_opponent(self, ):
    #     return

#     def make_legal_cards_list(self):
#         # cards that are specified as legal in this game
#         self.legal_cards = {"pokemon": {}, "trainers": {}}
#
#         for card_set in self.legal_cards_sets:
#             for card_type in "pokemon", "trainers":
#                 card_set_path = SETS_PATH / self.generation / card_set / f"{card_type}.yml"
#                 self.legal_cards[card_type].update(get_yml_data(card_set_path))
#
#     def show_legal_cards_list(self, card_type: str = None):
#         if card_type:
#             print(self.legal_cards[card_type])
#             return
#         print(self.legal_cards)
#
#     def make_available_decks_list(self):
#         generations_deck_folder = DECKS_PATH / self.generation
#         decks_found = generations_deck_folder.glob("*.yml")
#         # print(decks_found)
#         self.decks_available = {}
#         for deck in decks_found:
#             # print(deck)
#
#             deck_name = str(deck).split("/")[-1].replace(".yml", "")
#             print(deck_name)
#             self.decks_available[deck_name] = get_yml_data(deck)
#
#     def make_deck(self):
#
#         # Add legal energies TODO
#         pass
#
#     def set_player_deck(self, player_name: str, deck_of_choice: str):
#         self.players[player_name].set_deck(deck_of_choice)
#
#
#
#
# def get_generations_cards(generation: str, legal_card_sets: []) -> dict:
#     """  """
#     pass
#
#
#
#
#
#
# # def get_card_sets_pokemon(generation: str, card_set: str, card_type: str) -> dict:
# #     path = SETS_PATH / generation / card_set / f"{card_type}.yml"
# #     return get_yml_data(path)
#
#
# # def get_generations_pokemon(generation: str) -> dict:
# #     generations_pokemon = {}
# #     for card_set in SETS[generation]:
# #         generations_pokemon.update(get_card_sets_pokemon(generation, card_set, "pokemon"))
#
#     # return generations_pokemon
#
#
# def make_card_list():
#     # TODO get all pokemon from generation
#     # TODO get all trainers from generation
#
#     # TODO make list of pokemon objects
#     # TODO make list of trainer objects
#     pass
#
#
# def add_pokemon() -> list:
#     pass
#
#
# def add_trainers() -> list:
#     pass
#
#
# def add_energies() -> list:
#     pass
#
#
# def make_deck(deck_yml: pathlib.Path = None) -> list:
#     deck_list = get_yml_data(deck_yml)
#
#     deck = []
#     # deck += add_pokemon(deck_list["Pokemon"])
#     # deck += add_trainers(deck_list["Trainers"])
#     # deck += add_energies(deck_list["Energies"])
#
#     return deck
#
#
#
# def make_decks(generation: str = None) -> None:
#
#     for deck_name in DECKS.keys():
#         deck_path = pathlib.Path("")
#         deck = make_deck(deck_path)
#         DECKS[deck_name] = deck
#
#
# def pick_deck():
#     pass
#
#
#
#
# # make_card_list()
# # make_decks()
#
# the_game = Game("One", "Two", "gen1", ["base_set", "jungle"])
#
# the_game.make_legal_cards_list()
# # the_game.show_legal_cards_list("pokemon")
# # the_game.show_legal_cards_list("trainers")
# the_game.make_available_decks_list()
# print(the_game.decks_available['wavemaker'])


