import sqlite3

students = sqlite3.connect("students.sqlite")
cur1 = students.cursor()
cur1.execute("""CREATE TABLE IF NOT EXISTS students(
   familia TEXT,
   name TEXT,
   father TEXT,
   class TEXT,
   email TEXT,
   numbercard TEXT);
""")
students.commit()
information = ('Рябова', 'Екатерина', 'Николавна', '10В', 'riabovakate@yandex.ru', '1043110')
cur1.execute("INSERT INTO students (familia, name, father, class, email, numbercard) VALUES(?, ?, ?, ?, ?, ?)", information)
students.commit()
information = ('Поплавский', 'Даниил', 'Евгеньевич', '11Т', 'viKing17a@yandex.ru', '1717115')
cur1.execute("INSERT INTO students (familia, name, father, class, email, numbercard) VALUES(?, ?, ?, ?, ?, ?)", information)
students.commit()
information = ('Еленик', 'Татьяна', 'Ильинична', '10В', 'eleniktanya@gmail.com', '9090909')
cur1.execute("INSERT INTO students (familia, name, father, class, email, numbercard) VALUES(?, ?, ?, ?, ?, ?)", information)
students.commit()
information = ('Мкртчян', 'Алина', 'Никитична', '10В', 'alinamkr@yandex.ru', '2043110')
cur1.execute("INSERT INTO students (familia, name, father, class, email, numbercard) VALUES(?, ?, ?, ?, ?, ?)", information)
students.commit()
information = ('Поттер', 'Гарри', 'Джеймсович', '10В', 'harrypotter@yandex.ru', '1052110')
cur1.execute("INSERT INTO students (familia, name, father, class, email, numbercard) VALUES(?, ?, ?, ?, ?, ?)", information)
students.commit()
information = ('Андреев', 'Сергей', 'Анатольевич', '5Д', 'andreevs@yandex.ru', '1043250')
cur1.execute("INSERT INTO students (familia, name, father, class, email, numbercard) VALUES(?, ?, ?, ?, ?, ?)", information)
students.commit()
information = ('Яшина', 'Василиса', 'Константиновна', '5Д', 'vas@yandex.ru', '1009110')
cur1.execute("INSERT INTO students (familia, name, father, class, email, numbercard) VALUES(?, ?, ?, ?, ?, ?)", information)
students.commit()
information = ('Гончарова', 'Юлия', 'Денисовна', '10В', 'saweteen@yandex.ru', '7778123')
cur1.execute("INSERT INTO students (familia, name, father, class, email, numbercard) VALUES(?, ?, ?, ?, ?, ?)", information)
students.commit()
information = ('Гончарова', 'Юлия', 'Денисовна', '5Д', 'bzzzz@yandex.ru', '1234567')
cur1.execute("INSERT INTO students (familia, name, father, class, email, numbercard) VALUES(?, ?, ?, ?, ?, ?)", information)
students.commit()
information = ('Мкртчян', 'Георгий', 'Артемович', '11Т', 'goshan@gmail.com', '0000000')
cur1.execute("INSERT INTO students (familia, name, father, class, email, numbercard) VALUES(?, ?, ?, ?, ?, ?)", information)
students.commit()



