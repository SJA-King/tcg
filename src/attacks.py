from common import STATUSES


class Attack:
    def __init__(self,
                 name: str = "Attack",
                 energy_cost: dict = None,
                 damage: int = 0,
                 effect: str = None,
                 coin_flip: bool = False,
                 n_coin_flip: int = 0,
                 coin_flip_effect: str = ""):
        self.attack_name = name
        self.energy_cost = energy_cost
        self.damage = damage
        self.effect = effect
        self.coin_flip = coin_flip
        if self.coin_flip:
            if n_coin_flip <= 0:
                raise Exception("n_coin_flip must be >0")
        self.n_coin_flip = n_coin_flip
        self.coin_flip = coin_flip_effect
        pass

# TODO Make things like
# DamageAttack - which is an attack with just damage
# EffectAttack - which is an attack with just an effect
# SingleCoinFlipAttack - which is an attack with 1 coin flip
# SingleCoinFlipEffectAttack - which is an attack with just an effect with 1 coin flip
# DoubleCoinFlipAttack - which is an attack with 2 coin flip
# etc


# effect and coinflipeffect are the same, just one is bounded on coin flip

# TODO add common effects, like draw, burn energy, inflict_status, etc


# TODO attacks as methods
def confuse_ray():
    pass


# OR
# TODO attacks as classes and thus objects
# class ConfuseRay(Attack):
#
#     def __init__(self):
#         super().__init__(name="Confuse Ray", damage=30, coin_flip=True, n_coin_flip=1, coin_flip_effect=STATUSES["confuse"])
#         pass


# Have a look up like
ATTACKS = {
    # "Confuse Ray": confuse_ray()
    "Confuse Ray": Attack(name="Confuse Ray",
                          # TODO add energy in an enum style
                          energy_cost={"psychic": 3},
                          damage=30,
                          coin_flip=True,
                          n_coin_flip=1,
                          # TODO change to an enum style
                          coin_flip_effect=STATUSES["confuse"])
}
