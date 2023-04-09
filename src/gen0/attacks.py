# Make generic attacks in here, then in the gens they make them specific
# e.g.
from ..player import Player


class Attack:
    def __init__(self, name: str):
        __name__ = name

    def active_damage(self, reciever: Player, damage: int): # TODO add damage type!
        if damage % 10 != 0:
            raise Exception(f"Damage: {damage} ISNT multiple of ten")
        reciever.active.take_damage(damage=damage)  # TODO make this method

def benched_damage():
    pass

def active_status():
    pass

def set_status_sleep():
    pass
def set_status_paralyzed():
    pass
def set_status_():
    pass

