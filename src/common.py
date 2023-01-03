import random


def coin_flip(force_flip: int = None) -> bool:
    """ Simple Heads (true) or Tails (False) method"""
    flip = random.randint(0, 1)
    if force_flip:
        flip = force_flip
    if flip == 0:
        return True
    return False


# TODO move these, this isnt the right place for them
def give_sleep():
    pass


def give_confuse():
    pass


def give_paralysis():
    pass

# TODO for future generations
# def give_poison()
#     pass
#
# def give_burn():
#     pass

STATUSES = {
    "sleep": give_sleep(),
    "confuse": give_confuse(),
    "paralysis": give_paralysis()
}
