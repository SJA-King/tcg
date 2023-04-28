
from ..cards import Card

# Gust of Wind:
#   description: Choose 1 of your opponent's Benched Pokémon and switch it with his or her Active Pokémon.

def gust_of_wind():

    # TODO waste card if none on bench
    # TODO add a select bench position
    move_pokemon(self.other.active, self.other.bench)

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