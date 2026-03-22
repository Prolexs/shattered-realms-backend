class ItemStats:

    def __init__(

            self,

            damage=0,

            defense=0,

            hp=0,

            crit=0

    ):

        self.damage = damage

        self.defense = defense

        self.hp = hp

        self.crit = crit


    def __str__(self):

        return f"DMG:{self.damage} DEF:{self.defense} HP:{self.hp}"