# Make generic attacks in here, then in the gens they make them specific
# e.g.
from tcg.src.player import Player


class Attack:

    def active_damage(self, reciever: Player, damage: int):
        if damage % 10 != 0:
            raise Exception(f"Damage: {damage} ISNT multiple of ten")
        reciever.active.take_damage(damage=damage)

def benched_damage():

def active_status():

def set_status_sleep():
def set_status_paralyzed():
def set_status_():


