from tcg.src.gen0.attacks import *
from tcg.src.gen0.pokepowers import *

ATTACKS = {
    # TODO How do i pass in the object of the player?
    "Jab": active_damage(reciever="Active", damage=20)
}