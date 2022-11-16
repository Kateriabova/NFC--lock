from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, \
    QDialog, QTableWidgetItem
import sys
from student import Student
from kabinet import Kabinet
from klass import Klass
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, \
    QDialog, QTableWidget
import sys
import sqlite3


class Find(QMainWindow):
    def __init__(self, email):
        super().__init__()

        self.teacher_email = email
        uic.loadUi('ui/find.ui', self)
        self.choose.activated[str].connect(self.on_activated) #активация какой-то выборки
        self.find_btn.clicked.connect(self.find_some) #кнопка поиск
        self.students = sqlite3.connect("../db/students.sqlite")
        self.cur1 = self.students.cursor()
        self.y = False
        self.x = False #флажки

    def find_some(self): #поиск!
        self.x = True #флажок
        self.some = self.find_line.text()
        if not self.y: #активирована ли выборка?
            self.some = self.find_line.text() #что мы ищем
            students = sqlite3.connect("../db/students.sqlite")
            cur = students.cursor()
            if self.some == '':
                que = '''SELECT * from students'''
                data = cur.execute(que).fetchall() #это если мы ничего не ищем
            else:
                a = self.some.split()
                if len(a) == 1:
                    que = '''SELECT * from students WHERE students.familia = ?''' #поиск по фамилии
                    data = cur.execute(que, (a[0],)).fetchall()
                if len(a) == 2:
                    que = '''SELECT * from students WHERE students.familia = ? and students.name = ?''' #поиск по фамилии + имени
                    data = cur.execute(que, (a[0], a[1])).fetchall()
                if len(a) == 3:
                    que = '''SELECT * from students WHERE students.familia = ? and students.name = ? #поиск по фамилии-имени-отчеству
                           and students.father = ?'''
                    data = cur.execute(que, (a[0], a[1], a[3])).fetchall()
                else:
                    que = '''SELECT * from students'''
                    data = cur.execute(que).fetchall()
            self.table_find.setRowCount(len(data))
            self.table_find.setColumnCount(len(data[0]) + 2) #создали табличку

            for i, elem in enumerate(data):
                name = data[i][4] + "->"
                self.btn = QPushButton(name)
                self.btn.setMinimumSize(200, 0)
                self.btn.clicked.connect(self.study)
                self.table_find.setCellWidget(i, 0, self.btn) #кнопока в таблице указывает на объект
                self.btn.setObjectName(data[i][3])
            for j, elem in enumerate(data):
                for i, val in enumerate(elem):
                    self.table_find.setItem(j, i + 2, QTableWidgetItem(val)) #запихали результаты поиска в таблицу
        else:
            self.on_activated(self.text)

    def on_activated(self, text): #активирована выборка
        self.y = True #флажок
        self.text = text

        if text == 'ученик':
            students = sqlite3.connect("../db/students.sqlite")
            cur = students.cursor()
            if self.x:

                if self.some == '':
                    que = '''SELECT * from students''' #если ничего не ищем
                    data = cur.execute(que).fetchall()
                else:
                    a = self.some.split()
                    if len(a) == 1:

                        que = '''SELECT * from students WHERE students.familia = ?''' #поиск по фамилии
                        data = cur.execute(que, (a[0],)).fetchall()
                        b = 3
                    elif len(a) == 2:
                        que = '''SELECT * from students WHERE students.familia = ? and students.name = ?''' #поиск по фамилии-имени
                        data = cur.execute(que, (a[0], a[1])).fetchall()
                    elif len(a) == 3:
                        que = '''SELECT * from students WHERE students.familia = ? and students.name = ?  #поиск по фамилии-имени-отчеству
                               and students.father = ?'''
                        data = cur.execute(que, (a[0], a[1], a[3])).fetchall()
                    else:
                        que = '''SELECT * from students'''
                        data = cur.execute(que).fetchall() #ничего не ищем
            else:
                que = '''SELECT * from students'''
                data = cur.execute(que).fetchall() #если ничего не написано в строке поиск выводится все

            self.table_find.setRowCount(len(data))
            self.table_find.setColumnCount(len(data[0]) + 2)

            for i, elem in enumerate(data):
                name = data[i][4] + "->"
                self.btn = QPushButton(name)
                self.btn.setMinimumSize(200, 0)
                self.btn.clicked.connect(self.study)
                self.table_find.setCellWidget(i, 0, self.btn)
                self.btn.setObjectName(data[i][3]) #создание кнопки в таблице с указанием на объект
            for j, elem in enumerate(data):
                for i, val in enumerate(elem):
                    self.table_find.setItem(j, i + 2, QTableWidgetItem(val)) #создание таблицы
        if text == "кабинет": #поиск по кабинету
            kab = sqlite3.connect("../db/students.sqlite")
            cur = kab.cursor()
            if self.x:
                if self.some == '': #ищем все
                    que = '''SELECT * from kab'''
                    data = cur.execute(que).fetchall()
                else:

                    que = '''SELECT * from kab WHERE kab.number = ?'''#ищем определенный кабинет
                    data = cur.execute(que, (self.some,)).fetchall()

            else:
                que = '''SELECT * from kab''' #ищем все, так как не нажата кнопка поиск
                data = cur.execute(que).fetchall()

            self.table_find.setRowCount(len(data))
            self.table_find.setColumnCount(2)

            for i, elem in enumerate(data):
                name = data[i][0] + "->"
                self.btn = QPushButton(name)
                self.btn.clicked.connect(self.kabs)
                self.table_find.setCellWidget(i, 0, self.btn)  # (r, c)
                self.btn.setObjectName(data[i][0]) #кнопка с сслыкой на объект
            for j, elem in enumerate(data):
                self.table_find.setItem(j, 1, QTableWidgetItem(elem[0])) #заполняем табличку
        if text == 'класс': #если активирован "класс"
            students = sqlite3.connect("../db/students.sqlite")
            cur = students.cursor()
            if self.x:
                if self.some == '':
                    que = '''SELECT * from students'''
                    data = cur.execute(que).fetchall() #в строке поиска ничего нет, ищем все
                else:
                    que = '''SELECT * from students WHERE students.class = ?'''
                    data = cur.execute(que, (self.some.upper(),)).fetchall() #ищем определенный класс
            else:
                que = '''SELECT * from students'''
                data = cur.execute(que).fetchall() #кнопка поиска не активирована, ищем все

            self.table_find.setRowCount(len(data))
            self.table_find.setColumnCount(len(data[0]) + 1)

            for i, elem in enumerate(data):
                name = data[i][3] + "->"
                self.btn = QPushButton(name)
                self.btn.clicked.connect(self.classes)
                self.table_find.setCellWidget(i, 0, self.btn)
                self.btn.setObjectName(data[i][3]) #кнопка с ссылкой на объект
            for j, elem in enumerate(data):
                for i, val in enumerate(elem):
                    self.table_find.setItem(j, i + 1, QTableWidgetItem(val)) #наполняем табличку

    def study(self): #переход к нужному ученику
        x = self.sender()
        email = x.text()[:-2]
        students = sqlite3.connect("../db/students.sqlite")
        cur = students.cursor()

        que = '''SELECT * from students WHERE students.email = ?'''
        data = cur.execute(que, (email,)).fetchall()

        fio = {}
        f = ['familia', 'name', 'father', 'class', 'email']
        for i in range(len(f)):
            fio[f[i]] = data[0][i] #формирование набора данных для того, что бы закинуть их в объект нового класса
        self.st = Student(self.teacher_email, fio)
        self.close()
        self.st.show() #создание объекта класса студент и переход в новое окно

    def classes(self): #переход к нужному кабинету
        x = self.sender()
        num = x.text()[:-2]
        self.kl = Klass(self.teacher_email, num) #создание объекта класса и переход к нему
        self.close()
        self.kl.show()

    def kabs(self): #переход к кабинету
        x = self.sender()
        num = x.text()[:-2]
        kabs = sqlite3.connect("../db/students.sqlite")
        cur = kabs.cursor()

        que = '''SELECT * from kab WHERE number = ?''' #поиск нужного кабинета
        data = cur.execute(que, (num,)).fetchall()

        fio = {}
        f = ['number', 'foto']
        for i in range(len(f)):
            fio[f[i]] = 'db/' + data[0][i] #формирование набора данных, чтобы передать его в объект класса
        self.kb = Kabinet(self.teacher_email, fio)
        self.close()
        self.kb.show() #создание объекта класса каб и переход к нему
