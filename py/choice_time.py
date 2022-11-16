import sqlite3
import traceback

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, QDialog
import sys
import datetime as dt

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook

class Time(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/time.ui', self)
        c = [self.c0, self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8] #список check boxов
        self.numbers = [] #список номеров уроков
        self.time_1 = ''
        self.time_2 = '' #выбранное время на qtimeedit
        self.ok.clicked.connect(self.ret) #кнопка ок
        for i in c:
            i.clicked.connect(self.lesson) #если активировался какой то из чек-боксов


    def ret(self):
        a = str(dt.date.today()) #сегодняшняя дата
        t_1 = a + ' ' + self.time_since.text() + ':00'
        t_2 = a + ' ' + self.time_before.text() + ':00' #обработка данных из qtimeedit
        if t_1 != t_2: #проверка: выставлял ли в ручную пользователь время
            t = (t_1, t_2)
            self.times = [t] #если да, то есть первая пара начало-конец
        else:
            self.times = [] #если нет, то список временных промежутков пустой
        for i in self.numbers:
            le = sqlite3.connect("../db/students.sqlite")
            cur2 = le.cursor()
            que = '''SELECT * from lessons WHERE number = ?''' #подключение к базе данных времени уроков
            data = cur2.execute(que, (i,)).fetchall()
            b = data[0][1]
            e = data[0][2]
            t_1 = a + ' ' + b + ':00'
            t_2 = a + ' ' + e + ':00' #на основе этого создается время: дата + время по бд + секунды
            t = (t_1, t_2) #пара в кортеж, а тот - в список
            self.times.append(t)
        times = sqlite3.connect("../db/students.sqlite")
        cur2 = times.cursor()
        cur2.execute("""CREATE TABLE IF NOT EXISTS ti(
           time_b TEXT, 
           time_e TEXT);""") # подключаем временную бд по временным промежуткам
        times.commit()
        cur2.execute("""DELETE FROM ti""") #очищаем
        times.commit()
        for i in self.times:
            cur2.execute("INSERT INTO ti (time_b, time_e) VALUES(?, ?)", i)
            times.commit() #все промежутки аккуратно помещаем туда
        self.close() #успешно закрываем диалог

    def lesson(self): #активирован чек-бокс
        x = self.sender()
        a = x.text()[0] #номер урока, за который этот чек-боес отвечает
        if a not in self.numbers: #проверка состояния
            self.numbers.append(a) #либо добавляем этот номер урока
        else:
            self.numbers.remove(a) #либо удаляем


