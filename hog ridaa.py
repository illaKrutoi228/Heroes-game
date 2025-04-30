class ClashRoyal:
    def __init__(self, init_name):
        self.name = init_name

    def goblingang(self):
        print(f"PArty with the gobling Gang {self.name}")

    def noparte(self):
        print(f"Несподівано до {user_name} прибіг кабан.Паті віз зе гобрін генгс не буде😭😭😭😭 ")


user_name = input("Хог 2.6 чи Шустрі джентельмене 1.8? --->")
user_party = ClashRoyal(user_name)
x = input("Чи відбувся паті віз зе гоблінг генг? --->")
if x[0].upper() == "У":
    user_party.party()
else:
    user_party.noparte()