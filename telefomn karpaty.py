list["aaaaaaaaaaaa","bbbbbbbbbbbbbbbb","ccccccccccccc", "tttttttttt"]
res = None
x = input("Glisti v indexe -")

while True:
    try:
        print(list[int(x)])
        break
    except:
        print("DIBILOID")
        continue
