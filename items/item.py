from items.item_types import ItemType

from items.rarity import Rarity

from items.item_stats import ItemStats


class Item:

    def __init__(

            self,

            id:int,

            name:str,

            item_type:ItemType,

            rarity:Rarity,

            stats:ItemStats=None,

            stackable:bool=False

    ):

        self.id = id

        self.name = name

        self.type = item_type

        self.rarity = rarity

        self.stats = stats

        self.stackable = stackable

        self.quantity = 1


    def __str__(self):

        return f"{self.name} [{self.rarity.name}]"