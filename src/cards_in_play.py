from cards import Pokemon, Trainer, Energy
from attacks import Attacks
from pokepowers import PokePower
from attacks import Attacks

# Only an InPlay Card needs player_1 and player_2

# TODO PokemonInPlay has Cards attached to it, so we can move them around


class PokemonInPlay(Pokemon):
    _attached_energies: list[Energy] = []
    _attached_trainers: list[Trainer] = []
    _attached_pokemon: list[Pokemon] = []
    _damage_count: int = 0

    # TODO constructor needs (owner: Player, opponent: Player)

    def attack_x(self, number: int):
        if not self._attacks:
            raise Exception("No Attacks listed!")
        if len(self._attacks) > number:
            return Attacks[self._attacks[number]]
        return False

    def attack_one(self):
        return self.attack_x(0)

    def attack_two(self):
        return self.attack_x(1)

    def attack_three(self):
        return self.attack_x(2)

    # TODO think about how a Pokemon(Card) becomes a PokemonInPlay AND vice versa

    def take_damage(self, damage_amount: int):
        self._damage_count += damage_amount
        if self._damage_count > self._hit_points:
            # TODO discard to discard
            raise NotImplementedError

    def show_attached_energies(self):
        return self._attached_energies

    def show_attached_trainers(self):
        return self._attached_trainers

    def replace_attacks(self):
        pass

    def replace_pokepower(self, pokepowers: list[PokePower]):
        # TODO make a setter for these properties
        pass

    def replace_name(self, name: str):
        pass

    def evolve(self, evolving_card: Pokemon):
        if evolving_card.name != self.evolution_stage:
            raise Exception(f"{evolving_card.name} cant evolve into {self.evolution_stage}")
        self.replace_name(evolving_card.name)
        self.replace_pokepower(evolving_card.pokepower)
        # TODO ah make in_play_versions of basic card things, that way we can devolve



# x = PokemonInPlay(_attacks=["jab", "special_punch"])
# x.attack_one()


# TODO evolving a PokemonInPlay
# Changes name, hp, attacks, pokepower, weakness, etc

# TODO Need to set turn pokemon was 'laid'
# TODO need to set turn pokemon was 'evolved'
## TODO so you can compare current turn to laid_turn, evolved_turn and allow or dissallow
# TODO if user selects option evolve, then offer only PokemonInPlay that can evolve
## TODO if there are none, dont even offer option?

class ActivePokemon(PokemonInPlay):

    status = None

    pass

    def set_burn(self):
        raise NotImplementedError

    def set_confusion(self):
        raise NotImplementedError

    def set_sleep(self):
        raise NotImplementedError

    def set_paralsis(self):
        raise NotImplementedError

    def become_benched(self):
        # TODO check statuses?
        # TODO Switch bypasses
        if len(self.attached_energies) >= self.retreat_cost:
            # TODO
            raise NotImplementedError
        else:
            print("need more energy!")

    def become_active(self):
        raise NotImplementedError

    def devolve(self):
        raise NotImplementedError



class BenchedPokemon(PokemonInPlay):
    can_attack = False


    def become_active(self):

        pass


# class TrainerInPlay(Trainer):
#     pass
#
#
# class EnergyInPlay(Energy):
#     pass