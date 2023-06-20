from attacks import (Attack, jab, special_punch, thunderpunch, thundershock, leek_slap, pot_smash, scrunch, double_edge,
                     confuse_ray, wing_attack)
from common import EnergyTypes, EvoStages
from pokepowers import PokePower, damage_swap, prehistoric_power
from dataclasses import dataclass
from cards import Card, CardType, CardFlavour
from typing import final


@dataclass
class Pokemon(Card):
    energy_type: EnergyTypes = None
    resistance: EnergyTypes = None
    weakness: EnergyTypes = None

    attack_one: Attack = None
    attack_two: Attack = None
    attack_three: Attack = None
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
                          attack_one=jab(),
                          attack_two=special_punch(),
                          weakness=EnergyTypes.PSYCHIC,
                          retreat_cost=2),
    "Electabuzz": Pokemon(name="Electabuzz",
                          energy_type=EnergyTypes.LIGHTNING,
                          hit_points=70,
                          attack_one=thundershock(),
                          attack_two=thunderpunch(),
                          weakness=EnergyTypes.FIGHTING,
                          retreat_cost=2),
    "Far'fetchd": Pokemon(name="Far'fetchd",
                          energy_type=EnergyTypes.COLORLESS,
                          hit_points=50,
                          attack_one=leek_slap(),
                          attack_two=pot_smash(),
                          resistance=EnergyTypes.FIGHTING,
                          weakness=EnergyTypes.LIGHTNING,
                          retreat_cost=1),
    "Chansey": Pokemon(name="Chansey",
                       energy_type=EnergyTypes.COLORLESS,
                       hit_points=120,
                       attack_one=scrunch(),
                       attack_two=double_edge(),
                       resistance=EnergyTypes.PSYCHIC,
                       weakness=EnergyTypes.FIGHTING,
                       retreat_cost=1),
    "Alakazam": Pokemon(name="Alakazam",
                        energy_type=EnergyTypes.PSYCHIC,
                        hit_points=80,
                        attack_one=confuse_ray(),
                        pokepower=damage_swap(),
                        weakness=EnergyTypes.PSYCHIC,
                        retreat_cost=3,
                        evolution_stage=EvoStages.STAGE_TWO),
}
#alakazam:
##  number: 1
#  type: psychic
#  hit_points: 80
#  attack_1: Confuse Ray
##    name: confuse ray
##    energy_cost: [ psychic, psychic, psychic ]
##    effect: Flip a coin. If heads, the Defending Pokémon is now Confused.
##    damage: 30
#  weakness: psychic
#  retreat_cost: 3
#  pokepower: Damage Swap
#    effect: As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of
#      your Pokémon to another as long as you don't Knock Out that Pokémon. This power can't be used if Alakazam
#      is Asleep, Confused, or Paralyzed.
#  other:
#    #                        other non-game information
#    no: 065
#    height: 4'11" (1.5 m)
#    weight: 106 lbs. (48.0 kg)
#    pokedex_entry: Its brain can outperform a supercomputer. Its intelligence quotient is said to be 5000.


FOSSIL_POKEMON: final({str: Pokemon}) = {
    "Aerodactyl": Pokemon(name="Aerodactyl",
                          energy_type=EnergyTypes.FIGHTING,
                          hit_points=60,
                          attack_one=wing_attack(),
                          resistance=EnergyTypes.FIGHTING,
                          weakness=EnergyTypes.GRASS,
                          retreat_cost=2,
                          pokepower=prehistoric_power())
}

JUNGLE_POKEMON: final({str: Pokemon}) = {
    "Clefable": Pokemon(name="Clefable",
                        energy_type=EnergyTypes.COLORLESS,
                        hit_points=70,
                        # attack_one=Metronome,
                        # attack_two=Minimize,
                        resistance=EnergyTypes.PSYCHIC,
                        weakness=EnergyTypes.FIGHTING,
                        retreat_cost=2)
}

GEN1_POKEMON: final({str: Pokemon}) = {}
GEN1_POKEMON.update(BASE_POKEMON)
GEN1_POKEMON.update(JUNGLE_POKEMON)
GEN1_POKEMON.update(FOSSIL_POKEMON)
