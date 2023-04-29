# an Action is something that effects the game's board state

# An action handles contents of other classes, i.e. not a Player, but a players deck, hand, etc
from tcg.src.cards import Card
# class Action:
#
#     def __init__(self, name: str = "Action", action: str = None):
#         self.name = name
#         self.action = action


def move_cards_between_piles(from_pile: list[Card], to_pile: list[Card], number: int = 1) -> [list[Card], list[Card]]:
    """ Move 'number' of Cards from one Pile to another """
    if not from_pile:
        raise Exception(f"Pile '{from_pile}' is Empty")
    if number < 1:
        raise Exception(f"Incorrect number of Cards to move = '{number}'!")

    for n in range(number):
        to_pile.append(from_pile[0])
        from_pile.pop(0)

    return from_pile, to_pile


# TODO Do piles need to be objects?


def draw_cards(from_deck: list, to_hand: list, number: int = 1):  # DO I HAVE TO return?
    move_cards_between_piles(from_deck, to_hand, number)

def gain_prize(from_prizes: list, to_hand: list):
    move_cards_between_piles(from_prizes, to_hand)


# TODO or should this be

def draw_card(self, number: int = 1):
    move_cards_between_piles(self.current_player.deck, self.current_player.hand, number)





def select_cards(pile_to_select: list, number: int = 1) -> list:
    """ Select a pile of cards from another pile of cards """
    # TODO INCOMPLETE!
    return pile_to_select





ACTIONS = {
    # TODO Need to make this more generic
    # "Draw": Action("Draw", action=draw_card())
}
