import json

from config import SAVE_FILE


def save_player(player):

    data = {

        "name": player.name,

        "level": player.level,

        "hp": player.stats.hp,

        "damage": player.stats.damage

    }

    with open(SAVE_FILE,"w") as file:

        json.dump(data,file,indent=4)