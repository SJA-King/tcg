from .attacks import Attacks
from .common import EnergyTypes, EvoStages
from .pokepowers import PokePower, damage_swap, prehistoric_power
from dataclasses import dataclass
from .cards import Card, CardType, CardFlavour
from typing import final


@dataclass
class Pokemon(Card):
    energy_type: EnergyTypes = None
    resistance: EnergyTypes = None
    weakness: EnergyTypes = None

    attack_one: Attacks = None
    attack_two: Attacks = None
    attack_three: Attacks = None
    pokepower: PokePower = None

    hit_points: int = 0

    retreat_cost: int = None

    card_flavour: CardFlavour = CardFlavour.BASIC
    evolution_stage: EvoStages = EvoStages.BASIC

    def __post_init__(self):
        self.card_type = CardType.POKEMON


# TODO Change attacks to class objects of Attack!

BASE_POKEMON: final({str: Pokemon}) = {
    "Hitmonchan": Pokemon(name="Hitmonchan",
                          energy_type=EnergyTypes.FIGHTING,
                          hit_points=70,
                          attack_one=Attacks.Jab,
                          attack_two=Attacks.SpecialPunch,
                          weakness=EnergyTypes.PSYCHIC,
                          retreat_cost=2),
    "Electabuzz": Pokemon(name="Electabuzz",
                          energy_type=EnergyTypes.LIGHTNING,
                          hit_points=70,
                          attack_one=Attacks.Thundershock,
                          attack_two=Attacks.Thunderpunch,
                          weakness=EnergyTypes.FIGHTING,
                          retreat_cost=2),
    "Far'fetchd": Pokemon(name="Far'fetchd",
                          energy_type=EnergyTypes.COLORLESS,
                          hit_points=50,
                          attack_one=Attacks.LeekSlap,
                          attack_two=Attacks.PotSmash,
                          resistance=EnergyTypes.FIGHTING,
                          weakness=EnergyTypes.LIGHTNING,
                          retreat_cost=1),
    "Chansey": Pokemon(name="Chansey",
                       energy_type=EnergyTypes.COLORLESS,
                       hit_points=120,
                       attack_one=Attacks.Scrunch,
                       attack_two=Attacks.DoubleEdge,
                       resistance=EnergyTypes.PSYCHIC,
                       weakness=EnergyTypes.FIGHTING,
                       retreat_cost=1),
    "Alakazam": Pokemon(name="Alakazam",
                        energy_type=EnergyTypes.PSYCHIC,
                        hit_points=80,
                        attack_one=Attacks.ConfuseRay,
                        pokepower=damage_swap(),
                        weakness=EnergyTypes.PSYCHIC,
                        retreat_cost=3,
                        evolution_stage=EvoStages.STAGE_TWO),
}

FOSSIL_POKEMON: final({str: Pokemon}) = {
    "Aerodactyl": Pokemon(name="Aerodactyl",
                          energy_type=EnergyTypes.FIGHTING,
                          hit_points=60,
                          attack_one=Attacks.WingAttack,
                          resistance=EnergyTypes.FIGHTING,
                          weakness=EnergyTypes.GRASS,
                          retreat_cost=2,
                          pokepower=prehistoric_power())
}

JUNGLE_POKEMON: final({str: Pokemon}) = {
    "Clefable": Pokemon(name="Clefable",
                        energy_type=EnergyTypes.COLORLESS,
                        hit_points=70,
                        attack_one=Attacks.Metronome,
                        attack_two=Attacks.Minimize,
                        resistance=EnergyTypes.PSYCHIC,
                        weakness=EnergyTypes.FIGHTING,
                        retreat_cost=2)
}

GEN1_POKEMON: final({str: Pokemon}) = {}
GEN1_POKEMON.update(BASE_POKEMON)
GEN1_POKEMON.update(JUNGLE_POKEMON)
GEN1_POKEMON.update(FOSSIL_POKEMON)
