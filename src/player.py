# There are two players
# Each Player has a Deck, Hand, Discard, Prize_Pool
# Each Player has cards in play -> Active, Bench, Prize
from .piles import Deck
# from .gen0.actions import move_card
from .cards import Card, Trainer, Pokemon, Energy
from .actions import move_cards_between_piles, draw_cards, check_card_type_in_pile

from random import shuffle
from typing import Union, Type


class Player:

    def __init__(self, name):
        self._name = name
        self._deck: [Union[Trainer, Pokemon, Energy]] = []
        self._hand: [Union[Trainer, Pokemon, Energy]] = []
        self._prize_pool: [Union[Trainer, Pokemon, Energy]] = []
        self._active = None
        self._discard = []
        self._prizes_drawn = False
        self._hands_drawn = 0

    @property
    def name(self):
        return self._name

    @property
    def deck(self):
        return self._deck

    @property
    def hand(self):
        return self._hand

    @property
    def discard(self):
        return self._discard

    # TODO make this only settable once!
    # TODO add a lock?
    @deck.setter
    def deck(self, chosen_deck: list):
        if len(chosen_deck) != 60:
            raise Exception(f"Deck size ({len(chosen_deck)}) is incorrect")
        if not check_card_type_in_pile(card_type=Pokemon, pile=chosen_deck):
            raise Exception(f"Deck must have at least one {type(Pokemon)}!")
        # TODO check pokemon is basic as well otherwise ERROR!
        self._deck = chosen_deck
        self.shuffle_deck()

    def draw_cards(self, number: int):
        """ Move an amount of cards from player DESK pile to player HAND pile"""
        draw_cards(from_deck=self._deck, to_hand=self._hand, number=number)

    def draw_card(self):
        """ Move a card from the DESK pile to the HAND pile"""
        draw_cards(from_deck=self._deck, to_hand=self._hand)

    def shuffle_deck(self):
        shuffle(self._deck)

    def draw_hand(self):
        self.draw_cards(7)
        self._hands_drawn += 1

    def remake_deck(self):
        """
        Put all cards back into deck
        """
        self._deck = self._deck + self._hand + self._prize_pool + self._discard
        self._hand = []
        self._prize_pool = []
        self._discard = []
        assert len(self._deck) == 60, f"Deck size is incorrect: {len(self._deck)}"
        self.shuffle_deck()

    def redraw_hand(self):
        self.remake_deck()
        self.draw_hand()

    def show_hand(self):
        cards_in_hand = ""
        for i_card in self._hand:
            cards_in_hand += f"{i_card.name}, "
        return cards_in_hand

    def has_pokemon_in_hand(self) -> bool:
        return check_card_type_in_pile(card_type=Pokemon, pile=self._hand)

    def select_cards(self, pile_to_select_from, number: int = 1):
    #     TODO get player to pick
    #     return [pile_to_select_from[0]]
        raise NotImplementedError

    def discard_cards(self, selection: list) -> [list, list]:
        """ Move cards from a SELECTION pile to DISCARD pile"""
        for _ in range(len(selection)):
            selection, self.discard = move_card(from_pile=selection, to_pile=self.discard)

    def discard_deck_cards(self, number: int = 1):
        selected = self.select_cards(self._deck, number)
        self.discard_cards(selected)

    def discard_hand_cards(self, number: int = 1):
        selected = self.select_cards(self._hand, number)
        self.discard_cards(selected)

    def discard_cards_from_pokemon(self):
        # TODO discard all from a PokemonInPlay
        raise NotImplementedError

    def draw_prizes(self):
        if self._prizes_drawn:
            raise Exception("Cant draw prizes after Game has started")
        move_cards_between_piles(from_pile=self.deck, to_pile=self._prize_pool, number=6)
        self._prizes_drawn = True

    def take_prize(self, number: int = 1):
        # TODO give choice of 1, 2, 3, 4, 5, 6
        prize = self.select_cards(self._prize_pool, number=number)
        self._hand.append(prize)

    def has_empty_deck(self) -> bool:
        return len(self._deck) < 1

    # DOESNT WORK :/
    # TODO fix
    # def set_opponent(self, opponent: Player):
    #     # TODO either have each player know each other, OR have game know this
    #     self.opponent = opponent
