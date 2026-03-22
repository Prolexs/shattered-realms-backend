class Stats:

    def __init__(

            self,

            hp:int,

            damage:int,

            defense:int=0,

            crit:float=0

    ):

        self.hp = hp

        self.damage = damage

        self.defense = defense

        self.crit = crit


    def apply_item_bonus(self,item):

        if item.stats is None:

            return

        self.damage += item.stats.damage

        self.defense += item.stats.defense

        self.hp += item.stats.hp

        self.crit += item.stats.crit