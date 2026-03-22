import random

from items.item import Item

from items.item_types import ItemType

from items.rarity import Rarity

from items.item_stats import ItemStats


def generate_loot():

    loot_table = [

        Item(

            1,

            "Iron Sword",

            ItemType.WEAPON,

            Rarity.COMMON,

            ItemStats(damage=5)

        ),

        Item(

            2,

            "Steel Armor",

            ItemType.ARMOR,

            Rarity.RARE,

            ItemStats(defense=8,hp=15)

        ),

        Item(

            3,

            "Health Potion",

            ItemType.CONSUMABLE,

            Rarity.COMMON,

            stackable=True

        )

    ]

    return random.choice(loot_table)