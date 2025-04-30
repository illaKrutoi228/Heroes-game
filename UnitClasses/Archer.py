from .Unit import Unit
from .items import Abilities


class Archer(Unit):

    def __init__(self, init_name = "Archer", init_health_default = 700, init_attack_default = 150):
        self.name = init_name
        self.health_default = init_health_default
        self.attack_default = init_attack_default

        self.ability = Abilities("PoisonedArrow",50,"Does 50 damage to 1 enemy and unit for next to fights",3)