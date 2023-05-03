from cards import Pokemon, Trainer, Energy

# Only an InPlay Card needs player_1 and player_2

# TODO PokemonInPlay has Cards attached to it, so we can move them around


class PokemonInPlay(Pokemon):
    can_attack = True
    attached_energies = []
    attached_trainers = []
    retreat_cost = 0
    pass


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

    def evolve(self):
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