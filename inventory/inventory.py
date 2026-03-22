# Inventory system core module
from inventory.slot import InventorySlot

from config import INVENTORY_SIZE

from items.item import Item


class Inventory:

    def __init__(self):

        self.slots = [

            InventorySlot()

            for _ in range(INVENTORY_SIZE)

        ]

    # TODO add item stacking
    # TODO add weight system
    # TODO add inventory sorting
    # TODO add item filters
    def add_item(self,item:Item):

        # TODO add stacking logic

        for slot in self.slots:

            if slot.is_empty():

                slot.set_item(item)

                return True

        return False


    def remove_item(self,index:int):

        if index < 0 or index >= len(self.slots):

            return False

        self.slots[index].clear()

        return True

    # TODO add pagination
    # TODO add UI adapter
    def list_items(self):

        for i,slot in enumerate(self.slots):

            if not slot.is_empty():

                print(i,slot.item)


    def free_slots(self):

        count = 0

        for slot in self.slots:

            if slot.is_empty():

                count += 1

        return count