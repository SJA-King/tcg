import random


def coin_flip(force_flip: int = None) -> bool:
    """ Simple Heads (true) or Tails (False) method"""
    flip = random.randint(0, 1)
    if force_flip:
        flip = force_flip
    if flip == 0:
        return True
    return False
