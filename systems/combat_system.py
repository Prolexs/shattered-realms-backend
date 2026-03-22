from config import CRIT_CHANCE


def calculate_damage(player):

    base_damage = player.stats.damage

    weapon = player.equipment.weapon

    if weapon and weapon.stats:

        base_damage += weapon.stats.damage


    # TODO add armor mitigation
    # TODO add elemental damage


    return base_damage


def calculate_crit():

    import random

    roll = random.random()

    if roll <= CRIT_CHANCE:

        return True

    return False