# Make generic attacks in here, then in the gens they make them specific
# e.g.
# from .player import Player
# from .cards import Card, play_card


# def play_attack(card_name: str) -> None:
#     play_card(card_name)

# from .player import Player
from enum import Enum, auto
from .common import EnergyTypes
class Status(Enum):
    PARALYZED = auto()  # cant attack or retreat for 1 turn
    ASLEEP = auto()  # coin flip between turns, heads is awake, tails not
    CONFUSED = auto()  # coin flip to attack, heads as-normal, tails take 3 damage counters
    # below are future statuses
    # BURNED = auto()
    # POISONED = auto()

class CoinFlip(Enum):
    HEADS = True
    TAILS = False


class AttackEffects(Enum):
    DAMAGE = auto()
    DISCARD = auto()
    DRAW = auto()
    RECOIL = auto()
    IMMUNE = auto()
    PARALYZED = Status.PARALYZED
    ASLEEP = Status.ASLEEP
    CONFUSED = Status.CONFUSED

from typing import Union
class Attack:
    def __init__(self,
                 name: str,
                 active_damage: int = 0,
                 status: Status = None,
                 recoil_damage: int = 0,
                 discard: dict[EnergyTypes: int] = None,
                 immune: bool = False,
                 # TODO change EnergyTypes to EnergyCards!
                 cost: dict[EnergyTypes: int] = None,
                 coin_flip: int = 0,
                 heads_effect: AttackEffects = None,
                 tails_effect: AttackEffects = None
                 ):


    # def active_damage(self, receiver: Player, damage: int): # TODO add damage type!
    #     if damage % 10 != 0:
    #         raise Exception(f"Damage: {damage} ISNT multiple of ten")
    #     receiver.active.take_damage(damage=damage)  # TODO make this method

# Example attacks!
jab = Attack(name="Jab",
             active_damage=20,
             cost={EnergyTypes.FIGHTING: 1})
thundershock = Attack(name="Thundershock",
                      active_damage=10,
                      coin_flip=1,
                      heads_effect=AttackEffects.PARALYZED,
                      cost={EnergyTypes.LIGHTNING: 1}
                      )
thundpunch = Attack(name="Thunderpunch",
                    active_damage=30,
                    coin_flip=1,
                    heads_effect=AttackEffects.DAMAGE, # TODO set increased damage
                    tails_effect=AttackEffects.RECOIL,  # TODO set recoil damage
                    cost={EnergyTypes.LIGHTNING: 1, EnergyTypes.COLORLESS: 1})


# TODO maybe have an effect class? with damage_flat, damage_modifier, etc? Or could that be part of Attack?



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

def wing_attack():
    raise NotImplementedError


def confuse_ray():
    raise NotImplementedError


def jab():
    raise NotImplementedError


def double_edge():
    raise NotImplementedError


def leek_slap():
    raise NotImplementedError


def pot_smash():
    raise NotImplementedError


def scrunch():
    raise NotImplementedError


def special_punch():
    raise NotImplementedError


def thunderpunch():
    raise NotImplementedError


def thundershock():
    raise NotImplementedError


from enum import Enum


class Attacks(Enum):
    DoubleEdge = (double_edge,)
    Jab = (jab,)
    LeekSlap = (leek_slap,)
    PotSmash = (pot_smash,)
    Scrunch = (scrunch,)
    SpecialPunch = (special_punch,)
    Thunderpunch = (thunderpunch,)
    Thundershock = (thundershock,)
    WingAttack = (wing_attack,)
    ConfuseRay = (confuse_ray,)

    def __call__(self, *args, **kwargs):
        return self.value[0](*args, **kwargs)

# Works like below
# print(Attacks["jab"])
# >>Attacks.jab
# print(Attacks["jab"](1))
# >>World
# print(Attacks["jab"](0))
# >>Hello


