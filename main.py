from core.player import Player

from systems.loot_system import generate_loot

from systems.combat_system import calculate_damage

from logger import logger

from systems.save_system import save_player

player = Player("Alex")

logger.info("Player created")


for i in range(5):

    item = generate_loot()

    player.pickup_item(item)

    logger.info(f"Loot obtained: {item}")

    if item.type.name == "WEAPON":

        player.equip_item(item)

        logger.info("Weapon equipped")


player.show_inventory()


damage = calculate_damage(player)

logger.info(f"Player damage: {damage}")

save_player(player)

logger.info("Player saved")