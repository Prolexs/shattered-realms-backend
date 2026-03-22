from items.item import Item

from items.item_types import ItemType


class Equipment:

    def __init__(self):

        self.weapon: Item | None = None

        self.armor: Item | None = None


    def equip(self,item:Item):

        if item.type == ItemType.WEAPON:

            self.weapon = item

            return True


        if item.type == ItemType.ARMOR:

            self.armor = item

            return True


        return False


    def unequip_weapon(self):

        self.weapon = None


    def unequip_armor(self):

        self.armor = None