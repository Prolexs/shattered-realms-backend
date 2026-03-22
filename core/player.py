from inventory.inventory import Inventory

from inventory.equipment import Equipment

from core.stats import Stats

from config import BASE_HP, BASE_DAMAGE


class Player:

    def __init__(self,name:str):

        self.name = name

        self.level = 1

        self.stats = Stats(

            BASE_HP,

            BASE_DAMAGE

        )

        self.inventory = Inventory()

        self.equipment = Equipment()


    def pickup_item(self,item):

        return self.inventory.add_item(item)


    def equip_item(self,item):

        success = self.equipment.equip(item)

        if success:

            self.stats.apply_item_bonus(item)

        return success


    def show_inventory(self):

        self.inventory.list_items()