# There are two players
from dataclasses import dataclass
# Each Player has a Deck, Hand, Discard, Prize_Pool
# Each Player has cards in play -> Active, Bench, Prize
from .piles import Deck, Pile, Hand, Prizes, Discard
# from piles import Deck, Pile, Hand, Prizes, Discard
# from .gen0.actions import move_card
from .cards import Card, Trainer, Pokemon, Energy
# TODO make game do the action upon Player not the player doing them
from .actions import (move_cards_between_piles, draw_cards, check_card_type_in_pile, draw_prizes, take_prize,
                      draw_starting_hand, move_cards, put_prizes_back_into_deck,
                      put_hand_back_into_deck, put_discard_back_into_deck, check_pokemon_is_basic)
from .cards_in_play import PokemonInPlay, ActivePokemon, BenchedPokemon
from .common import EvoStages

from random import shuffle
from typing import Union, Type


@dataclass
class Player:

    def __init__(self, name, chosen_deck: Deck):
        self._name = name
        # self._deck: [Union[Trainer, Pokemon, Energy]] = []
        # self._hand: [Union[Trainer, Pokemon, Energy]] = []
        # self._prize_pool: [Union[Trainer, Pokemon, Energy]] = []
        # self._discard = []
        self.deck: Deck = chosen_deck
        self.hand: Hand = Hand([])
        self.prizes: Prizes = Prizes([])
        self.discard: Discard = Discard([])
        self._active: ActivePokemon = ActivePokemon()
        self._hands_drawn = 0
        self.prizes_drawn = False
        self._ready = False

    @property
    def name(self):
        return self._name

    @property
    def hands_drawn(self):
        return self._hands_drawn

    @property
    def ready(self):
        return self._ready

    def is_ready(self) -> None:
        print(f"Player: {self.name} (Ready) : Drawn '{self.hands_drawn}' hands")
        self._ready = True
    #
    # @property
    # def hand(self):
    #     return self._hand
    #
    # @property
    # def discard(self):
    #     return self._discard

    # # TODO make this only settable once!
    # # TODO add a lock?
    # @deck.setter
    # def deck(self, chosen_deck: list):
    #     if len(chosen_deck) != 60:
    #         raise Exception(f"Deck size ({len(chosen_deck)}) is incorrect")
    #     # TODO add the below check to Deck class!
        # if not check_card_type_in_pile(card_type=Pokemon, pile=chosen_deck):
        #     raise Exception(f"Deck must have at least one {type(Pokemon)}!")
        # TODO check pokemon is basic as well otherwise ERROR!
        # self._deck = chosen_deck
        # self.shuffle_deck()

    def draw_cards(self, number: int = 1):
        """ Move an amount of cards from player DESK pile to player HAND pile"""
        draw_cards(from_deck=self.deck, to_hand=self.hand, number=number)

    def draw_card(self):
        """ Move a card from the DESK pile to the HAND pile"""
        self.draw_cards()

    # TODO stop random shuffling!
    def shuffle_deck(self):
        self.deck.shuffle()
        # shuffle(self._deck)

    def put_hand_back_into_deck(self):
        put_hand_back_into_deck(self.hand, self.deck)

    def put_discard_back_into_deck(self):
        put_discard_back_into_deck(self.discard, self.deck)

    def put_prizes_back_into_deck(self):
        put_prizes_back_into_deck(self.prizes, self.deck)

    def remake_deck(self):
        self.put_hand_back_into_deck()
        self.put_discard_back_into_deck()
        self.put_prizes_back_into_deck()
        # TODO put active back into deck
        # TODO put benched back into deck
        self.shuffle_deck()

    # TODO maybe need to change these names
    def draw_hand(self):
        draw_starting_hand(self.deck, self.hand)
        print(f"{self.name} - Hand = {self.show_hand()}")
        self._hands_drawn += 1

    def redraw_hand(self):
        self.remake_deck()
        self.draw_hand()

    def show_hand(self):
        cards_in_hand = ""
        for i_card in self.hand.cards:
            cards_in_hand += f"{i_card.name}, "
        return cards_in_hand

    def has_pokemon_in_hand(self) -> bool:
        pokemon_in_hand = check_card_type_in_pile(card_type=Pokemon, pile=self.hand)
        if pokemon_in_hand:
            return check_pokemon_is_basic(pokemon_in_hand)

        return False

    def select_cards(self, pile_to_select_from, number: int = 1):
    #     TODO get player to pick
    #     return [pile_to_select_from[0]]
        raise NotImplementedError

    # def discard_cards(self, selection: list) -> [list, list]:
    #     """ Move cards from a SELECTION pile to DISCARD pile"""
    #     for _ in range(len(selection)):
    #         selection, self.discard = move_card(from_pile=selection, to_pile=self.discard)

    # def discard_deck_cards(self, number: int = 1):
    #     selected = self.select_cards(self._deck, number)
    #     self.discard_cards(selected)
    #
    # def discard_hand_cards(self, number: int = 1):
    #     selected = self.select_cards(self._hand, number)
    #     self.discard_cards(selected)

    def discard_cards_from_pokemon(self):
        # TODO discard all from a PokemonInPlay
        raise NotImplementedError

    def draw_prizes(self):
        print(f"{self.name} draw prizes")
        if self.prizes_drawn:
            raise Exception("Cant draw prizes after Game has started")

        draw_prizes(from_deck=self.deck, to_prizes=self.prizes)
        # move_cards_between_piles(from_pile=self.deck, to_pile=self._prize_pool, number=6)
        self.prizes_drawn = True

    def take_prize(self, number: int = 1):
        # TODO give choice of 1, 2, 3, 4, 5, 6
        prize = self.select_cards(self.prizes, number=number)
        take_prize(self.prizes, self.hand)
        # self._hand.append(prize)

    def has_empty_deck(self) -> bool:
        return self.deck.cards_left()

    # DOESNT WORK :/
    # TODO fix
    # def set_opponent(self, opponent: Player):
    #     # TODO either have each player know each other, OR have game know this
    #     self.opponent = opponent
