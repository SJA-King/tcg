# an Action is something that effects the game's board state

# class Action:
#
#     def __init__(self, name: str = "Action", action: str = None):
#         self.name = name
#         self.action = action


def move_card(from_pile: list, to_pile: list) -> [list, list]:
    """ Move a single card from one pile to another """
    if len(from_pile) < 1:
        raise Exception(f"From pile: {from_pile} is empty!")
    from_pile.pop()
    to_pile.append(from_pile[0])
    return from_pile, to_pile


# def move_cards(from_pile: list, to_pile: list, number: int = 1) -> [list, list]:
#     """ Move multiple cards from one pile to another """
#     for n in range(number):
#         from_pile, to_pile = move_card(from_pile, to_pile)
#     return from_pile, to_pile





def select_cards(pile_to_select: list, number: int = 1) -> list:
    """ Select a pile of cards from another pile of cards """
    # TODO INCOMPLETE!
    return pile_to_select





ACTIONS = {
    # TODO Need to make this more generic
    "Draw": Action("Draw", action=draw_card())
}
