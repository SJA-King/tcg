from cards import Pokemon, Trainer, Energy

# Only an InPlay Card needs player_1 and player_2


class PokemonInPlay(Pokemon):
    can_attack = True
    attached_energies = []
    attached_trainers = []
    retreat_cost = 0
    pass


class ActivePokemon(PokemonInPlay):

    status = None

    pass

    def set_burn(self):
        pass

    def set_confusion(self):
        pass

    def set_sleep(self):
        pass

    def set_paralsis(self):
        pass

    def become_benched(self):
        # TODO check statuses?
        # TODO Switch bypasses
        if len(self.attached_energies) >= self.retreat_cost:
            # TODO
            pass
        else:
            print("need more energy!")

    def become_active(self):
        pass

    def evolve(self):
        pass

    def devolve(self):
        pass



class BenchedPokemon(PokemonInPlay):
    can_attack = False


    def become_active(self):

        pass


class TrainerInPlay(Trainer):
    pass


class EnergyInPlay(Energy):
    pass