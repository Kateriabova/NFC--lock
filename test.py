import sqlite3

students = sqlite3.connect("db/students.sqlite")
cur = students.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students(
   mail_of_student TEXT,
   kab TEXT,
   mail_of_teacher TEXT,
   data_since TEXT,
   data_before TEXT);""")

students.commit()
que = '''SELECT * from students'''
data = cur.execute(que).fetchall()
for i in data:
    print(i)