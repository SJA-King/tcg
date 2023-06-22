from enum import Enum, auto
from typing import Any
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
    STATUS = auto()
    # PARALYZED = Status.PARALYZED
    # ASLEEP = Status.ASLEEP
    # CONFUSED = Status.CONFUSED
    REDUCE = auto()
    METRONOME = auto()


class Attack:
    def __init__(self,
                 name: str,
                 damage: int = 0,
                 damage_multi: int = 0,
                 damage_modifier: int = 0,
                 effect: AttackEffects = None,
                 effect_value: Any = None,
                 # status: Status = None,
                 # recoil_damage: int = 0,
                 discard: dict[EnergyTypes: int] = None,
                 # immune: bool = False,
                 # TODO change EnergyTypes to EnergyCards!
                 cost: dict[EnergyTypes: int] = None,
                 coin_flips: int = 0,
                 heads_effect: AttackEffects = None,
                 heads_value: Any = None,
                 tails_effect: AttackEffects = None,
                 tails_value: Any = None,
                 turn_recharge: bool = False
                 ):
        self._name = name
        self._coin_flips = coin_flips

    @property
    def name(self):
        return self._name

    @property
    def coin_flips(self):
        return self._coin_flips


class Attacks(Enum):
    Jab = Attack(name="Jab",
                 damage=20,
                 cost={EnergyTypes.FIGHTING: 1})
    SpecialPunch = Attack(name="Special Punch",
                          damage=40,
                          cost={EnergyTypes.FIGHTING: 2,
                                EnergyTypes.COLORLESS: 1})
    Thundershock = Attack(name="Thundershock",
                          damage=10,
                          coin_flips=1,
                          heads_effect=AttackEffects.STATUS,
                          heads_value=Status.PARALYZED,
                          cost={EnergyTypes.LIGHTNING: 1}
                          )
    Thunderpunch = Attack(name="Thunderpunch",
                          damage=30,
                          coin_flips=1,
                          heads_effect=AttackEffects.DAMAGE,
                          heads_value=10,
                          tails_effect=AttackEffects.RECOIL,
                          tails_value=10,
                          cost={EnergyTypes.LIGHTNING: 1,
                                EnergyTypes.COLORLESS: 1})
    LeekSlap = Attack(name="Leek Slap",
                      damage=50,
                      turn_recharge=True,
                      cost={EnergyTypes.COLORLESS: 1})
    PotSmash = Attack(name="Pot Smash",
                      damage=50,
                      cost={EnergyTypes.COLORLESS: 3})
    Scrunch = Attack(name="Scrunch",
                     coin_flips=1,
                     heads_effect=AttackEffects.IMMUNE,
                     cost={EnergyTypes.COLORLESS: 2})
    DoubleEdge = Attack(name="Double-Edge",
                        damage=80,
                        effect=AttackEffects.RECOIL,
                        effect_value=80,
                        cost={EnergyTypes.COLORLESS: 4})
    ConfuseRay = Attack(name="Confuse Ray",
                        damage=30,
                        coin_flips=1,
                        heads_effect=AttackEffects.STATUS,
                        heads_value=Status.CONFUSED,
                        cost={EnergyTypes.PSYCHIC: 3})
    WingAttack = Attack(name="Wing Attack",
                        damage=30,
                        cost={EnergyTypes.COLORLESS: 3})
    Metronome = Attack(name="Metronome",
                       effect=AttackEffects.METRONOME,
                       cost={EnergyTypes.COLORLESS: 1})
    Minimize = Attack(name="Minimize",
                      effect=AttackEffects.REDUCE,
                      effect_value=20,
                      cost={EnergyTypes.COLORLESS: 2})

    def __call__(self, *args, **kwargs):
        return self.value[0](*args, **kwargs)

# Works like below
# print(Attacks["jab"])
# >>Attacks.jab
# print(Attacks["jab"](1))
# >>World
# print(Attacks["jab"](0))
# >>Hello
