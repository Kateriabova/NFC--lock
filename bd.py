import sqlite3

students = sqlite3.connect("students.sqlite")
cur1 = students.cursor()
cur1.execute("""CREATE TABLE IF NOT EXISTS users(
   familia TEXT,
   name TEXT,
   father TEXT,
   class TEXT,
   email TEXT,
   numbercard TEXT);
""")
students.commit()
information =
cur1.execute("INSERT INTO users (pupillogin, pupilpassword) VALUES(?, ?)", inf)
users.commit()

with open('students.csv', 'r', encoding='utf-8') as file_1:
    stud_bd = csv.reader(file_1, delimiter=';')
    y = True
    name = input()
    god_0 = input().split()
    god_1 = god_0[1]
    god_0 = god_0[0]
    stroki = list(filter(lambda y: y[1] == name, stroki))

    stroki = list(map(lambda z: [z[0], z[int(god_0) - 2013], z[int(god_1) - 2013]], stroki))

    stroki = list(filter(lambda q: (int(q[2]) * 100) // int(q[1]) < 104, stroki))
    if len(stroki) == 0:
        y = False
    a = [['Субъект', god_0, god_1]]
    stroki = list(map(lambda d: ';'.join(d), a + stroki))
    if y:
        res.write('\n'.join(stroki))
