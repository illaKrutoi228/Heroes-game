import abc
from .items import *

class Unit(abc.ABC):

    name = ""
    ability = None

    attack_default = 0
    attack_with_weapon = property()

    health_default = 0
    health_with_armor = property()
    health_in_fight = 0

    weapon = Weapon()

    helmet = Armor()
    bodyarmor = Armor()
    boots = Armor()
    shield = Armor()

    status = "Alive"

    magic_shield = False

    stunned = False

    poisoned_moves = 3
    poison_damage = 50

    @attack_with_weapon.getter
    def attack_with_weapon(self):
        a = self.attack_default + self.weapon.value
        return a


    @health_with_armor.getter
    def health_with_armor(self):
        h = self.health_default + self.helmet.value + self.bodyarmor.value + self.shield.value
        return h

    @staticmethod
    def check_all_effects(func):

        def wrapper(self, enemy):

            if self.poisoned_moves > 0:
                print(f"{self.name} is poisoned for {self.poisoned_moves} moves.")
                self.poisoned_moves -= 1
                self.health_in_fight -= self.poison_damage

            if self.stunned == True:
                print(f"{self.name} is stuned and cant do everything.")
                self.stunned = False
                return

            if enemy.magic_shield == True:
                print(f"{enemy.name} has magic shield.No damage taken.")
                enemy.magic_shield = False

                return func(self,enemy)

        return wrapper

    @check_all_effects
    def hit(self, enemy):

        enemy.health_in_fight -= self.attack_with_weapon
        if enemy.health_in_fight <= 0:
            enemy.health_in_fight = 0
            enemy.status = "Dead"
        print(f"{self.name} hit {enemy.name} by {self.attack_with_weapon}.")
    def unit_info(self):
        print(f"[{self.status}] Name: {self.name}, health: {self.health_in_fight}, attack: {self.attack_with_weapon}")