import Team
import Fight
import time

class Arena():
    def __init__(self, init_p_team, init_arena_counter):
        self.player_team = init_p_team
        self.arena_counter = init_arena_counter
        self.comp_team = Team.Team()

    def start_arena(self):
        self.comp_team.c_r_c_t()
        self.u_c_t_by_a_c()
        self.arena_s_board()
        time.sleep(5)
        self.arena_set_health()
        self.arena_fight()
        self.arena_f_board()
        self.arena_lvlup()

    def u_c_t_by_a_c(self):
        pass
        # Доробити різні прокачки для всіх героїв команди
        for unit in self.comp_team.team:
            if self.arena_counter == 1:
                pass
            if self.arena_counter == 2:
                pass

    def arena_lvlup(self):
        for unit in self.player_team.alive_team:
            unit.health_default *= 1.2
            #Левел ап для всіх героїв виживших з нашої команди

    def arena_set_health(self):
        for team in [self.player_team, self.comp_team]:
            for unit in team.team:
                unit.health_in_fight = unit.health_with_armor

    def arena_s_board(self):

        print(f'''
                    -----------------------------------------------------
                     ***** ARENA #{self.arena_counter} BOARD *******
                    -----------------------------------------------------
                                Welcome to the Arena!
                    {self.player_team.name}    VS     {self.comp_team.name}
                    ''')
        print("PLAYER TEAM")
        self.player_team.team_info()

        print()
        print("COMPUTER TEAM")
        self.comp_team.team_info()
        
    def arena_f_board(self):
        time.sleep(2.5)
        print(f'''
                         -----------------------------------------------------
                        ***** ARENA #{self.arena_counter} FINAL BOARD *******
                         -----------------------------------------------------
                         {self.player_team.name}    VS     {self.comp_team.name}
                         ''')
        print("PLAYER TEAM")
        self.player_team.team_info()

        print()
        print("COMPUTER TEAM")
        self.comp_team.team_info()

        if len(self.player_team.alive_team) == 0 and len(self.comp_team.alive_team) == 0:
            winner = None
            time.sleep(1)
            print("ALL ARE DEAD")
        elif len(self.player_team.alive_team) != 0:
            winner = self.player_team
        else:
            winner = self.comp_team

            if winner == None:
                time.sleep(1)
                print("ALL ARE DEAD!")
            else:
                time.sleep(2.5)

                print(f"The winner of #{self.arena_counter} Arena is :{self.winner.name}")

                time.sleep(2)
                print(f"ALIVE UNTS of {winner.name},squad:")
                winner.alive_team.team_info()

                print()

                time.sleep(2)
                print(f"DEAD UNTS of {winner.name},squad:")
                winner.dead_team.team_info()

                time.sleep(1)
                print("-------------------------------------------------------")


    def arena_fight(self):
        fight_counter=1

        while len(self.player_team.alive_team) != 0 and len(self.comp_team.alive_team):

            if fight_counter % 2 != 0:
                time.sleep(0.5)
                print("Player - choose your fighter!")
                self.player_team.team_info(True)
                player_unit = self.player_team.c_u_by_p()

                print()
                print("Player - choose your enem`ys to fight! ")
                self.comp_team.team_info(True)
                comp_unit = self.comp_team.c_u_by_p()



            else:
                comp_unit = self.comp_team.c_random_u()
                player_unit = self.player_team.c_random_u()

                print(comp_unit.name)
                print(player_unit.name)


            fight = Fight.Fight(player_unit, comp_unit, fight_counter, self.player_team, self.comp_team)
            fight.start_fight()


            fight_counter += 1
            time.sleep(1)

