import random
import UnitClasses
import time

class Team:
    alive_team = property()
    dead_team = property()

    def __init__(self, init_name = "NoName", init_team = []):
        self.name = init_name
        self.team = init_team

    @alive_team.getter
    def alive_team(self):
        result = []
        for u in self.team:
            if u.status == "Alive":
                result.append(u)
        return result

    @dead_team.getter
    def dead_team(self):
        result = []
        for u in self.team:
            if u.status == "Dead":
                result.append(u)
        return result

    def c_u_by_p(self):
        unit = None

        while not unit:
            x = input("Choose unit index -")

            try :
                print()
                unit = self.team[int(x)]
            except:
                time.sleep(1)
                print()
                print("This unit does`nt exist in this arena!Try another!")

        return unit



    def team_info(self, choosing = False):

        time.sleep(1)
        print(f'''
         ------------------------
            {self.name}
         ------------------------
            ''')

        if len(self.dead_team) == 0:
            for u in self.alive_team:
                if choosing == True:
                    print(self.alive_team.index(u), end = ")  ")
                u.unit_info()

        elif len(self.alive_team) == 0:
            time.sleep(1)
            print("ALL VARIORS ARE DEAD")
        else:
            time.sleep(1)
            print("ALIVE:")
            for u in self.alive_team:
                if choosing == True:
                    print(self.alive_team.index(u), end=")  ")
                u.unit_info()
            time.sleep(1)
            print("DEAD:")
            for u in self.dead_team:
                u.unit_info()
            print()

    def c_r_c_t(self):
        all_names = ["Bandites pubertatos team",
                    "Mope Karpatu team",
                    "Dnepr MT team",
                    "Suzuki team",
                    "Pubertats team",
                    "Korsike team",
                    "Minsk 125 team",
                    "Zhivchik sqad",
                    "Dristuletos team"
                        ]
        self.name = random.choice(all_names)


        all_units = [UnitClasses.Archer,
                     UnitClasses.Knight,
                     UnitClasses.Artillery,
                     UnitClasses.Defender,
                     UnitClasses.Wizard,
                     UnitClasses.Medic]

        for i in range(5):
             self.team.append(random.choice(all_units)())

    def c_random_u(self):
        return random.choice(self.alive_team)