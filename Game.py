import UnitClasses
import Fight
import time
import colorama
import Team
import Arena
import Shop


class Game():
    player_name = None
    player_gold = 1000
    all_arenas = 5
    arena_counter = 0
    player_team = None
    shop = None
    game_result = None

    def s_board(self):
        print(colorama.Fore.RED +'''
---------------------------------------------------------------------------------------------------       
        ******************************GAME OF HEROS********************************   
---------------------------------------------------------------------------- -----------------------
             -- by me with help
____________________________________________________________________________________________________
        ''')
        print()
        self.player_name = input("Type your name,for you command! ---->")
        time.sleep(1)
        print(colorama.Fore.BLUE + f'''
Welcome to the arena,{self.player_name}!
Here is some money,({self.player_gold}),to begin the your first arena!
Spend them to promote your team,to win them all!I believe in you {self.player_team},good luck! ''')
        time.sleep(1)

        self.player_team = Team.Team()

        start_team = [UnitClasses.Knight(),
                      UnitClasses.Medic(),
                      UnitClasses.Artillery(),
                      UnitClasses.Defender()]
        self.player_team.team.extend(start_team)

    def up_team(self):
        pass



    def start_game(self):
        self.s_board()

        while self.arena_counter < self.all_arenas:
            shop = Shop.Shop(self.player_team, self.player_gold)
            game_after_shop=shop.welcome_board()
            if game_after_shop == False:
                self.game_result = False
                break

            arena = Arena.Arena(self.player_team, self.arena_counter)
            arena.start_arena()

            if len(self.team.alive_team) < 0:
                self.game_result = False
                break

            self.arena_counter += 1
            self.up_team()

        if self.team_result == False:
            self.w_board()
        elif self.game_result == True:
            self.l_board()

game = Game()
game.start_game()