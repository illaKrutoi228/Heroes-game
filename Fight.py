import time

class Fight:
    def __init__(self,init_player_unit,init_comp_unit,init_fight_counter, init_player_team, init_comp_team):
        self.player_unit = init_player_unit
        self.comp_unit = init_comp_unit
        self.fight_counter = init_fight_counter
        self.player_team = init_player_team
        self.comp_team = init_comp_team


    def start_fight(self):
        self.dsb()
        self.hitmaker()
        self.dfb()


    def dsb(self):
        time.sleep(1.5)
        print(f'''
        ____________________
        FIGHT FOR US COUNTRY
        Nomer:{self.fight_counter}
        --------------------
        Player       Computer
        {self.player_unit.name}        {self.comp_unit.name}
        
        LET`S THE FIGHT BEGIN!
        ''')

    def use_ability(self, unit, enemy, unit_team, enemy_team):

        unit.ability.cooldown_left = unit.ability.cooldown

        if unit.name == "Artillery":
            print(f"{unit.name} makes SUPERATTACK! ")
            hit = unit.ability.value * unit.attack_with_weapon
            enemy.health_in_fight -= hit
            print(f"{unit.name} hits {enemy.name} by {hit}")

        elif unit.name == "Medic":
            print(f"{unit.name} makes SUPERHEAL! ")
            for u in unit_team.alive_team:
                heal = unit.ability.value * u.health_with_armor
                u.health += heal
                print(f"---> {u.name} was healed by {heal}hp")

        elif unit.name == "Knight":
            print(f"{unit.name} makes SPLASHATTACK!")
            for u in enemy_team.alive_team:
                hit = unit.ability.value * unit.attack_with_weapon
                for u in enemy_team.alive_team:
                    u.health_in_fight -= hit
                    print(f"---> {unit.name} hits {u.name} by {hit}")

        elif unit.name == "Wizard":
            print(f"{unit.name} makes SUPERSTUNE!")
            for u in enemy_team.alive_team:
                u.stunned = True
                print(f"{u.name} was stunned for 1 move")

        elif unit.name == "Defender":
            print(f"{unit.name} makes SUPERSHIELD!")
            for u in enemy_team.alive_team:
                u.magic_shield = True
                print(f"{u.name} gets magic shield")

        elif unit.name == "Archer":
            print(f"{unit.name} makes POISONED ARROW!")
            enemy.poison_moves = 3
            enemy.poison_damage = unit.ability.value

    def comp_check_abilities(self,player_unit,comp_unit,player_team,comp_team):
        if comp_unit.ability.cooldown_left > 0:
            comp_unit.ability.cooldown_left -= 1
        else:
            print(f"{comp_unit.name} uses its ability {comp_unit.ability.name}")
            self.use_ability(comp_unit, player_unit, comp_team, player_team)

    def player_check_abilities(self,player_unit,comp_unit, player_team, comp_team):
        if player_unit.ability.cooldown_left > 0:
            player_unit.ability.cooldown_left -= 1
        else:
            print(f"{player_unit.name} uses its ability {player_unit.ability.name}")
            while True:
                answer = input("Do you want to use ability? -")
                if not len(answer) or answer.upper()[0] not in["Y", "N"]:
                    continue
                elif answer.upper()[0] == "N":
                    return
                elif answer.upper()[0] == "Y":
                    self.use_ability(player_unit, comp_unit, player_team, comp_team)

    def hitmaker(self):
        self.player_check_abilities(self.player_unit,self.comp_unit,self.player_team,self.comp_team)
        self.player_unit.hit(self.comp_unit)

        self.comp_check_abilities(self.player_unit,self.comp_unit,self.player_team,self.comp_team)
        self.comp_unit.hit(self.player_unit)

    def dfb(self):
        print()
        self.player_unit.unit_info()
        self.comp_unit.unit_info()
        print()
        time.sleep(0.5)
        print("-"*25)