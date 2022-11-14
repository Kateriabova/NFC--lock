import sqlite3
from random import random

le = sqlite3.connect("db/lessons.sqlite")
cur2 = le.cursor()
cur2.execute("""CREATE TABLE IF NOT EXISTS accesses(
   number TEXT,
   time_b TEXT, 
   time_e TEXT);""")

le.commit()
information = ('1', '8:30', '9:15')
cur2.execute("INSERT INTO accesses (number, time_b, time_e) VALUES(?, ?, ?)", information)
le.commit()

information = ('2', '9:25', '10:10')
cur2.execute("INSERT INTO accesses (number, time_b, time_e) VALUES(?, ?, ?)", information)
le.commit()

information = ('3', '10:30', '11:15')
cur2.execute("INSERT INTO accesses (number, time_b, time_e) VALUES(?, ?, ?)", information)
le.commit()

information = ('4', '11:35', '12:20')
cur2.execute("INSERT INTO accesses (number, time_b, time_e) VALUES(?, ?, ?)", information)
le.commit()
information = ('5', '12:35', '13:20')
cur2.execute("INSERT INTO accesses (number, time_b, time_e) VALUES(?, ?, ?)", information)
le.commit()

information = ('6', '13:35', '14:20')
cur2.execute("INSERT INTO accesses (number, time_b, time_e) VALUES(?, ?, ?)", information)
le.commit()

information = ('7', '14:35', '15:20')
cur2.execute("INSERT INTO accesses (number, time_b, time_e) VALUES(?, ?, ?)", information)
le.commit()
information = ('8', '15:30', '16:15')
cur2.execute("INSERT INTO accesses (number, time_b, time_e) VALUES(?, ?, ?)", information)
le.commit()
information = ('9', '16:25', '17:10')
cur2.execute("INSERT INTO accesses (number, time_b, time_e  ) VALUES(?, ?, ?)", information)
le.commit()


