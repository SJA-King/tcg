
from .cards import Card, play_card
# from .player import Player
# from .actions import flip_heads, make_pkmn_in_play_active, make_pkmn_in_play_benched


# TODO in game.py
# def play_trainer():
#   Trainer.action(playee, opponent)
#   discard_card_from_hand(Trainer) # which under the hood moves it from hand to discard!



def play_trainer(card_name: str) -> None:
    play_card(card_name)

# TODO need a trainer class i think

# Gust of Wind:
#   description: Choose 1 of your opponent's Benched Pokémon and switch it with his or her Active Pokémon.

# TODO add energy retrieval

def gust_of_wind():
        # playee: Player, opponent: Player):
    pass
    # TODO waste card if none on bench
    # TODO add a select bench position
    # make_pkmn_in_play_benched(opponent)
    # move_pokemon(self.other.active, self.other.bench)


def computer_search():

    # TODO is discard implicit?
    # TODO check you CAN discard 2 cards!
    discard_cards(self.hand, self.discard, number=2)
    # TODO check deck isnt empty
    chosen_card: Card = select(self.deck)
    shuffle_pile(self.deck)
    move_cards([chosen_card], self.hand)



# Computer Search:
#   description: Discard 2 of the other cards from your hand in order to search your deck for any card and put it into your hand. Shuffle your deck afterward.


# Scoop Up:
#   description: Choose 1 of your Pokémon in play and return its Basic Pokémon card to your hand. (Discard all cards attached to that card.)
# TODO note its the basic card!!


# Defender:
#   description: Attach Defender to 1 of your Pokémon. At the end of your opponent's next turn, discard Defender. Damage done to that Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).


# PlusPower:
#   description: Attach PlusPower to your Active Pokémon. At the end of your turn, discard PlusPower. If this Pokémon's attack does damage to the Defending Pokémon (after applying Weakness and Resistance), the attack does 10 more damage to the Defending Pokémon.

def professor_oak():
    # TODO need to differientiate between discarding from hand AND from a Card(Pokemon, Energy, Trainer) in play
    discard(self.hand, number = MAX_HAND_SIZE)
    draw()
# Professor Oak:
#   description: Discard your hand, then draw 7 cards.
#   player: self
#   discard: 60  # 60 is used as MAXIMUM, meaning ALL
#   position_a: hand
#   draw: 7  # discard HAS to happen before draw though!
#
# Each top level key is the 'name' - then each trainer has a set of keys with values that are imported into its dataclass
# form e.g. Bill 'move's 2 cards from player:self's position_a:deck to postion_b:hand
#
# move: is a number from 1 - 60
# player: is 'self' or 'other'
#
# Bill:
#   description: Draw 2 cards.
#   move: 2
#   position_a: deck
#   position_b: hand
#   player: self # not self = other
# Energy Removal:
#   description: Choose 1 Energy card attached to 1 of your opponent's Pokémon and discard it.
#   discard: 1
#   player: other
#   position_a: active
#   card_type: energy
#
# Switch:
#   description: Switch 1 of your Benched Pokémon with your Active Pokémon.
# Item Finder:
#   description: Discard 2 of the other cards from your hand in order to put a Trainer card from your discard pile into your hand.
# Super Energy Removal:
#   description: Discard 1 Energy card attached to 1 of your own Pokémon in order to choose 1 of your opponent's Pokémon and up to 2 Energy cards attached to it. Discard those Energy cards.
# Use the keywords? Draw, Switch, Choose, Discard, Attach, etc?

#
# Fossil Trainers
#
#
# Mr Fuji:
#   description: Choose a Pokémon on your Bench. Shuffle it and any cards attached to it into your deck.
# Energy Search:
#   description: Search your deck for a basic Energy card and put it into your hand. Shuffle your deck afterward.
def do_gambler():
    """
    Gambler:
      description: Shuffle your hand into your deck. Flip a coin. If heads, draw 8 cards. If tails, draw 1 card.
    :return:
    """
    shuffle_deck()
    if flip_heads():
        draw_cards(8)
    else:
        draw_cards(1)

def do_recycle():
    """
    Recycle:
        description: Flip a coin. If heads, put a card in your discard pile on top of your deck.
    :return:
    """
    if flip_heads():
        selected_cards = select_cards(discard, number=1)
        # TODO Make a put on top of pile AND put on bottom of pil
        # TODO make a put on top of deck
        put_on_top_of_deck(selected_cards)


def do_mysterious_fossil():
    """
    Mysterious Fossil:
      description: Play Mysterious Fossil as if it were a Basic Pokémon. While in play, Mysterious Fossil counts as a Pokémon (instead of a Trainer card). Mysterious Fossil has no attacks, can't retreat, and can't be Asleep, Confused, Paralyzed, or Poisoned. If Mysterious Fossil is Knocked Out, it doesn't count as a Knocked Out Pokémon. (Discard it anyway.) At any time during your turn before your attack, you may discard Mysterious Fossil from play.
    """
    raise NotImplementedError


#
# Jungle Trainer
#
def do_poke_ball():
    """
    Poke Ball:
        text:
    """
    raise NotImplementedError

from .cards import CardType

from dataclasses import dataclass
# TODO below to change things to enums maybe
@dataclass
class Trainer(Card):
    #if so we could just have 'move' rather than 'draw' and / or 'discard'
    discard: int = 0
    draw: int = 0
    move: int = 0
    # NEED draw, discard and move, to make things easier!
    heal: bool = False
    switch: bool = False  # Used to swap active and bench OR active to hand
    player: str = ""
    # TODO need a position_from and a _to -- a to b?
    position_from: str = ""
    position_to: str = ""
    # position on its own is singular space? or should it always be a->b?
    position: str = ""  # E.g. hand, active, bench, deck, discard_pile
    attach: bool = False
    card_type = CardType.TRAINER
    # TODO need a select? rather than automatic?