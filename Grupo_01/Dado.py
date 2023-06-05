import random


def Launch(force: str) -> int:
    force = force.lower()
    if force == "debil":
        return random.randint(1, 3)
    elif force == "normal":
        return random.randint(1, 6)
    elif force == "fuerte":
        return random.randint(4, 6)
    return 0
