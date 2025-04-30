import sqlite3

def create_shop():
    db = sqlite3.connect("Shop_DB.db")
    cursor = db.cursor()

    #crwsarrweee
    cursor.execute('''CREATE TABLE IF NOT EXISTS item_types(
                        id TEXT PRIMARY KEY,
                        name TEXT
                        )''')
    cursor.execute("INSERT INTO item_types VALUES ('it1', 'units')")
    cursor.execute("INSERT INTO item_types VALUES ('it2', 'armor')")
    cursor.execute("INSERT INTO item_types VALUES ('it3', 'weapons')")
    cursor.execute("INSERT INTO item_types VALUES ('it4', 'abilities')")

    #cdc4rcrcgtr9u7sryru
    cursor.execute('''CREATE TABLE IF NOT EXISTS units(
                        id TEXT PRIMARY KEY,
                        item_type TEXT,
                        name TEXT,
                        price INTEGER
                        )''')
    cursor.execute("INSERT INTO units VALUES ('u1','it1', 'Knight',300)")
    cursor.execute("INSERT INTO units VALUES ('u2','it1', 'Medic',300)")
    cursor.execute("INSERT INTO units VALUES ('u3','it1', 'Artillery',300)")
    cursor.execute("INSERT INTO units VALUES ('u4','it1', 'Defender',300)")
    cursor.execute("INSERT INTO units VALUES ('u5','it1', 'Wizard',300)")
    cursor.execute("INSERT INTO units VALUES ('u6','it1', 'Archer',300)")


    #vjindn.jqqqqqqqatrmiotr\
    cursor.execute('''CREATE TABLE IF NOT EXISTS armor(
                            id TEXT PRIMARY KEY,
                            item_type TEXT,
                            name TEXT,
                            usable_for_unit TEXT,
                            value INTEGER,
                            price INTEGER
                            )''')

    cursor.execute("INSERT INTO armor VALUES ('ar1','it2','wooden helmet','ALL', 100, 400) ")
    cursor.execute("INSERT INTO armor VALUES ('ar2','it2','iron helmet','ALL', 200, 600) ")
    cursor.execute("INSERT INTO armor VALUES ('ar3','it2','steel helmet','ALL', 400, 800) ")

    cursor.execute("INSERT INTO armor VALUES ('ar4','it2','wooden bodyarmor','ALL',100, 500) ")
    cursor.execute("INSERT INTO armor VALUES ('ar5','it2','iron bodyarmor','ALL',250, 700) ")
    cursor.execute("INSERT INTO armor VALUES ('ar6','it2','steel bodyarmor','ALL',400, 1000) ")

    cursor.execute("INSERT INTO armor VALUES ('ar7','it2','wooden boots','ALL',50, 300) ")
    cursor.execute("INSERT INTO armor VALUES ('ar8','it2','iron boots','ALL',100, 500) ")
    cursor.execute("INSERT INTO armor VALUES ('ar9','it2','steel bodyarmor','ALL',200, 700) ")

    cursor.execute("INSERT INTO armor VALUES ('ar10','it2','wooden shield','ALL',100, 350) ")
    cursor.execute("INSERT INTO armor VALUES ('ar11','it2','iron shield','ALL',200, 650) ")
    cursor.execute("INSERT INTO armor VALUES ('ar12','it2','steel shield','ALL',300, 900) ")

 #cceeerwwwwwweppppppppppppppppppppppppppppppppppannnnnnnpnsssssssssssss
    cursor.execute('''CREATE TABLE IF NOT EXISTS weapons(
                               id TEXT PRIMARY KEY,
                               item_type TEXT,
                               name TEXT,
                               usable_for_unit TEXT,
                               value INTEGER,
                               price INTEGER
                               )''')

    cursor.execute("INSERT INTO weapons VALUES ('wp1','it3','wooden sword','u1', 100, 700) ")
    cursor.execute("INSERT INTO weapons VALUES ('wp2','it3','iron sword','u1', 350, 1100) ")
    cursor.execute("INSERT INTO weapons VALUES ('wp3','it3','steel sword','u1', 400, 1700) ")

    cursor.execute("INSERT INTO weapons VALUES ('wp4','it3','wooden knifes','u2', 100, 500) ")
    cursor.execute("INSERT INTO weapons VALUES ('wp5','it3','iron knifes','u2', 300, 800) ")
    cursor.execute("INSERT INTO weapons VALUES ('wp6','it3','steel knifes','u2', 600, 1200) ")

    cursor.execute("INSERT INTO weapons VALUES ('wp7','it3','stone projectails','u3', 250, 1000) ")
    cursor.execute("INSERT INTO weapons VALUES ('wp8','it3','iron projectails','u3', 600, 1500) ")
    cursor.execute("INSERT INTO weapons VALUES ('wp9','it3','explodives projectails','u3', 750, 2200) ")

    cursor.execute("INSERT INTO weapons VALUES ('wp10','it3','wooden morgenshtern','u4', 150, 700) ")
    cursor.execute("INSERT INTO weapons VALUES ('wp11','it3','iron morgenshtern','u4', 300, 800) ")
    cursor.execute("INSERT INTO weapons VALUES ('wp12','it3','steel morgenshtern','u4', 60, 1200) ")

    cursor.execute("INSERT INTO weapons VALUES ('wp13','it3','wooden knifes','u5', 100, 500) ")
    cursor.execute("INSERT INTO weapons VALUES ('wp14','it3','iron knifes','u5', 300, 800) ")
    cursor.execute("INSERT INTO weapons VALUES ('wp15','it3','steel knifes','u5', 60, 1200) ")

    cursor.execute("INSERT INTO weapons VALUES ('wp16','it3','wooden knifes','u6', 100, 500) ")
    cursor.execute("INSERT INTO weapons VALUES ('wp17','it3','iron knifes','u6', 300, 800) ")
    cursor.execute("INSERT INTO weapons VALUES ('wp18','it3','steel knifes','u6', 60, 1200) ")

    cursor.execute('''CREATE TABLE IF NOT EXISTS abilities(
                               id TEXT PRIMARY KEY,
                               item_type TEXT,
                               name TEXT,
                               usable_for_unit TEXT,
                               value INTEGER,
                               price INTEGER)''')

    cursor.execute("INSERT INTO abilities VALUES ('ab1','it3','Splash training lvl1','u1', 100, 700) ")
    cursor.execute("INSERT INTO abilities VALUES ('ab2','it3','Splash training lvl2','u1', 350, 1100) ")
    cursor.execute("INSERT INTO abilities VALUES ('ab3','it3','Splash training lvl3','u1', 400, 1700) ")

    cursor.execute("INSERT INTO weapons VALUES ('ab4','it3','wooden knifes','u2', 100, 500) ")
    cursor.execute("INSERT INTO weapons VALUES ('ab5','it3','iron knifes','u2', 300, 800) ")
    cursor.execute("INSERT INTO weapons VALUES ('ab6','it3','steel knifes','u2', 600, 1200) ")

    cursor.execute("INSERT INTO weapons VALUES ('ab7','it3','stone projectails','u3', 250, 1000) ")
    cursor.execute("INSERT INTO weapons VALUES ('ab8','it3','iron projectails','u3', 600, 1500) ")
    cursor.execute("INSERT INTO weapons VALUES ('ab9','it3','explodives projectails','u3', 750, 2200) ")

    cursor.execute("INSERT INTO weapons VALUES ('ab10','it3','wooden morgenshtern','u4', 150, 700) ")
    cursor.execute("INSERT INTO weapons VALUES ('ab11','it3','iron morgenshtern','u4', 300, 800) ")
    cursor.execute("INSERT INTO weapons VALUES ('ab12','it3','steel morgenshtern','u4', 60, 1200) ")

    cursor.execute("INSERT INTO weapons VALUES ('ab13','it3','wooden knifes','u5', 100, 500) ")
    cursor.execute("INSERT INTO weapons VALUES ('ab14','it3','iron knifes','u5', 300, 800) ")
    cursor.execute("INSERT INTO weapons VALUES ('ab15','it3','steel knifes','u5', 60, 1200) ")

    cursor.execute("INSERT INTO weapons VALUES ('ab16','it3','wooden knifes','u6', 100, 500) ")
    cursor.execute("INSERT INTO weapons VALUES ('ab17','it3','iron knifes','u6', 300, 800) ")
    cursor.execute("INSERT INTO weapons VALUES ('ab18','it3','steel knifes','u6', 60, 1200) ")

    db.commit()
    db.close()


create_shop()