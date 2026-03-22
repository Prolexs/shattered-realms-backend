from items.item import Item


class InventorySlot:

    def __init__(self):

        self.item: Item | None = None


    def is_empty(self):

        return self.item is None


    def set_item(self,item:Item):

        self.item=item


    def clear(self):

        self.item=None