from .Unit import Unit
from .items import Abilities


class Defender(Unit):

    def __init__(self, init_name = "Defender", init_health_default = 700, init_attack_default = 150):
        self.name = init_name
        self.health_default = init_health_default
        self.attack_default = init_attack_default

        self.ability = Abilities("Shield", 1, "Creats shield for all teamets, for next enemy unit hits,and reflect some damage", 4)