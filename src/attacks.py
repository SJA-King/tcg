# Make generic attacks in here, then in the gens they make them specific
# e.g.
from tcg.src.player import Player
from .cards import Card, play_card


def play_attack(card_name: str) -> None:
    play_card(card_name)


class Attack:
    def __init__(self, name: str):
        __name__ = name

    def active_damage(self, receiver: Player, damage: int): # TODO add damage type!
        if damage % 10 != 0:
            raise Exception(f"Damage: {damage} ISNT multiple of ten")
        receiver.active.take_damage(damage=damage)  # TODO make this method

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


# from ..common import STATUSES
# # from ..gen0.actions import Action
# from ..gen0.attacks import Attack
# from ..player import Player
#
# # Attacks build off actions
#
# # TODO fix this
# class Attack(Action):
#     def __init__(self,
#                  name: str = "Attack",
#                  energy_cost: dict = None,
#                  damage: int = 0,
#                  effect: str = None,
#                  coin_flip: bool = False,
#                  n_coin_flip: int = 0,
#                  coin_flip_effect: str = ""):
#         super().__init__(name, effect)
#
#         self.energy_cost = energy_cost
#         self.damage = damage
#         self.coin_flip = coin_flip
#         if self.coin_flip:
#             if n_coin_flip <= 0:
#                 raise Exception("n_coin_flip must be >0")
#         self.n_coin_flip = n_coin_flip
#         self.coin_flip = coin_flip_effect
#         pass
#
#     def use(self):
#         raise NotImplementedError
#
# # TODO Make things like
# # DamageAttack - which is an attack with just damage
# # EffectAttack - which is an attack with just an effect
# # SingleCoinFlipAttack - which is an attack with 1 coin flip
# # SingleCoinFlipEffectAttack - which is an attack with just an effect with 1 coin flip
# # DoubleCoinFlipAttack - which is an attack with 2 coin flip
# # etc
#
# # effect and coinflipeffect are the same, just one is bounded on coin flip
#
# # TODO add common effects, like draw, burn energy, inflict_status, reduce_damage, etc
#
# # TODO effects like add damage, reduce damage are used by trainers and attacks, so it should be generic!
#
# # def confuse_ray():
# #     pass
#
#
# # OR
# # TODO attacks as classes and thus objects
# # class ConfuseRay(Attack):
# #
# #     def __init__(self):
# #         super().__init__(name="Confuse Ray", damage=30, coin_flip=True, n_coin_flip=1, coin_flip_effect=STATUSES["confuse"])
# #         pass
#
#
# # Have a look up like
# ATTACKS = {
#     # "Confuse Ray": confuse_ray()
#     "Confuse Ray": Attack(name="Confuse Ray",
#                           # TODO add energy in an enum style
#                           energy_cost={"psychic": 3},
#                           damage=30,
#                           coin_flip=True,
#                           n_coin_flip=1,
#                           # TODO change to an enum style
#                           coin_flip_effect=STATUSES["confuse"]),
#     "Thundershock": Attack(),
#     "Thunderpunch": Attack(),
#     "Leek Slap": Attack(),
#     "Pot Smash": Attack(),
#     "Scrunch": Attack(),
#     "Double-edge": Attack(),
#     "Jab": Attack(),
#     "Special Punch": Attack(),
#     "None": None
# }
#
#
# def jab(receiver: Player):
#     Attack("jab").active_damage(reciever=receiver, damage=20)
#
