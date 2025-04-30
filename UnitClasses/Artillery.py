from .Unit import Unit
from .items import Abilities


class Artillery(Unit):

    def __init__(self, init_name = "Artillery", init_health_default = 700, init_attack_default = 150):
        self.name = init_name
        self.health_default = init_health_default
        self.attack_default = init_attack_default

        self.ability = Abilities("SuperAttack", 2,"Hits x2 damage to chosen enemy unit", 4)