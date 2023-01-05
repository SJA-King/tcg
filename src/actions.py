# an Action is something that effects the game's board state

class Action:

    def __init__(self, name: str = "Action", action: str = None):
        self.name = name
        self.action = action


ACTIONS = {
    "Draw": Action("Draw")
}
