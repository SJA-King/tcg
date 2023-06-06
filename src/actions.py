# an Action is something that effects the game's board state

# An action handles contents of other classes, i.e. not a Player, but a players deck, hand, etc
from .cards import Card, Pokemon, Trainer, Energy
from .piles import Deck, Hand, Discard, Pile, Prizes
from .common import EvoStages

import random
from typing import Union, Type
import typing


def flip_heads() -> bool:
    """
    1 = Heads
    2 = Tails
    :return:
    """
    if random.randint(1, 2) == 1:
        return True
    return False


# Unlikely to be needed but still useful
def flip_tails() -> bool:
    return not flip_heads()


def flip_multiple_heads(number: int = 1) -> int:
    if number < 1:
        raise Exception(f"Cant flip <1 COINS!")

    counter = 0
    for _ in range(number):
        if flip_heads():
            counter += 1

    return counter


# TODO make a check_pile()

# TODO change to put on bottom or append to pile?
def move_cards_between_piles(from_pile: list[Card], to_pile: list[Card], number: int = 1) -> [list[Card], list[Card]]:
    """ Move 'number' of Cards from one Pile to another """
    if not from_pile:
        raise Exception(f"Pile '{from_pile}' is Empty")
    if number < 1:
        raise Exception(f"Incorrect number of Cards to move = '{number}'!")

    for _ in range(number):
        to_pile.append(from_pile[0])
        from_pile.pop(0)

    return from_pile, to_pile


def move_cards(from_pile: Pile, to_pile: Pile, number: int = 1) -> None:
    """ Move 'number' of Cards from one Pile to another """
    if not from_pile:
        print("From Pile is Empty!")
        return
        # raise Exception(f"Pile '{from_pile}' is Empty")
    if len(from_pile.cards) == 0:
        print(f"From Pile is Empty!")
        return
    if number < 1:
        raise Exception(f"Cant move less than 1 Cards - '{number}'!")

    # TODO Add if number >= 60 that you just add them together dont loop!

    for _ in range(number):
        if from_pile.cards:
            card_to_move = from_pile.cards[0]
            to_pile.cards.append(card_to_move)
            from_pile.cards.pop(0)
        else:
            break


def draw_cards(from_deck: Deck, to_hand: Hand, number: int = 1):
    move_cards(from_pile=from_deck, to_pile=to_hand, number=number)


def check_hand_for_pokemon(hand: Hand):
    return check_card_type_in_pile(card_type=Pokemon, pile=hand)


def check_hand_for_basic_pokemon():
    raise NotImplementedError


def put_pile_back_into_deck(from_pile: Pile, to_deck: Deck):
    if type(to_deck) is not Deck:
        raise Exception("Expected Type Deck")
    if len(from_pile.cards) == 0:
        return
    move_cards(from_pile=from_pile, to_pile=to_deck, number=60)


def put_hand_back_into_deck(hand: Hand, deck: Deck):
    if type(hand) is not Hand:
        raise Exception("Expected Type Hand")
    put_pile_back_into_deck(hand, deck)


def put_discard_back_into_deck(discard: Discard, deck: Deck):
    if type(discard) is not Discard:
        raise Exception("Expected Type Discard")
    put_pile_back_into_deck(discard, deck)


def put_prizes_back_into_deck(prizes: Prizes, deck: Deck):
    if type(prizes) is not Prizes:
        raise Exception("Expected Type Prizes")
    put_pile_back_into_deck(prizes, deck)


def draw_starting_hand(from_deck: Deck, to_hand: Hand):
    if len(from_deck.cards) != 60:
        raise Exception(f"Starting Deck should have 60 cards - it has {from_deck.cards}")
    move_cards(from_pile=from_deck, to_pile=to_hand, number=7)


def put_all_cards_back_into_deck(deck: Deck, hand: Hand, discard: Discard, prizes: Prizes):
    move_cards(from_pile=hand, to_pile=deck, number=60)
    move_cards(from_pile=discard, to_pile=deck, number=60)
    move_cards(from_pile=prizes, to_pile=deck, number=60)

    deck.shuffle()


# def redraw_starting_hand(deck: Deck, hand: Hand, discard: Discard, prizes: Prizes):
#     put_all_cards_back_into_deck()
#
#     draw_starting_hand(from_deck=deck, to_hand=hand)


def discard_from_hand(from_hand: Hand, to_discard: Discard, number: int = 1):
    move_cards(from_pile=from_hand, to_pile=to_discard, number=number)


def discard_from_deck(from_deck: Deck, to_discard: Discard, number: int = 1):
    move_cards(from_pile=from_deck, to_pile=to_discard, number=number)


def draw_prizes(from_deck: Deck, to_prizes: Prizes):
    move_cards(from_pile=from_deck, to_pile=to_prizes, number=6)


def take_prize(from_prizes: Prizes, to_hand: Hand, number: int = 1):
    move_cards(from_pile=from_prizes, to_pile=to_hand, number=number)


def put_card_on_top_of_pile(from_pile: list[Card], to_pile: list[Card], number: int = 1):
    for _ in range(number):
        to_pile = [from_pile[0]] + to_pile
        from_pile.pop(0)


# def draw_cards(from_deck: list, to_hand: list, number: int = 1):  # DO I HAVE TO return?
#     move_cards_between_piles(from_deck, to_hand, number)


def gain_prize(from_prizes: list, to_hand: list):
    move_cards_between_piles(from_prizes, to_hand)


# TODO or should this be

def draw_card(self, number: int = 1):
    move_cards_between_piles(self.current_player.deck, self.current_player.hand, number)


def check_card_type_in_pile(card_type: Type[Card], pile: Pile) -> typing.Union[list[Card], bool]:
    if not pile:
        print("Empty Pile")
        return False
    cards_with_type = []
    for card in pile.cards:
        if card_type == type(card):
            cards_with_type.append(card)

    if not cards_with_type:
        return False
    return cards_with_type


def check_pokemon_is_basic(cards: list[Card]):
    # TODO fix unresolved attribute issue below - this 'typing.Union[Pile, Pokemon]' didnt work
    for card in cards:
        if type(card) is Pokemon:
            if card.evolution_stage == EvoStages.BASIC:
                return True

    return False


def select_cards(pile_to_select: list, number: int = 1) -> list:
    """ Select a pile of cards from another pile of cards """
    # TODO INCOMPLETE!
    return pile_to_select


# TODO make an action_builder using the string from the yml
# TODO make the build check the function exists as well!
# TODO use a function factory!!!
#
# >>> def func_builder(name):
# ...  def f():
# ...   # multiline code here, using name, and using the logic you have
# ...   return name
# ...  return f
# ...
# >>> func_builder("ciao")()
# 'ciao'




ACTIONS = {
    # TODO Need to make this more generic
    # "Draw": Action("Draw", action=draw_card())
}
