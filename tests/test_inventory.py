from inventory.inventory import Inventory

from items.item import Item

from items.item_types import ItemType

from items.rarity import Rarity


def test_inventory_add():

    inventory = Inventory()

    item = Item(

        1,

        "Test Sword",

        ItemType.WEAPON,

        Rarity.COMMON

    )

    result = inventory.add_item(item)

    assert result == True