from .Unit import Unit
from .items import Abilities


class Medic(Unit):

    def __init__(self, init_name = "Medic", init_health_default = 700, init_attack_default = 150):
        self.name = init_name
        self.health_default = init_health_default
        self.attack_default = init_attack_default

        self.ability = Abilities("Healing mates", 0.2,"He can heal al teammates by 20% from they max health ",3)