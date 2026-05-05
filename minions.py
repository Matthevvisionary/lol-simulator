class Minion:
    def __init__(self, name, hp, ad, md, ar, mr):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.md = md
        self.ar = ar
        self.mr = mr

caster_minion = Minion("Caster Minion", 300, 10, 0, 0, 10)
melee_minion = Minion("Melee Minion", 450, 0, 10, 10, 0)
cannon_minion = Minion("Cannon Minion", 800, 25, 0, 0, 0)