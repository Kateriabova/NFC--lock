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
        self.choose.activated[str].connect(self.on_activated)
        self.find_btn.clicked.connect(self.find_some)
        self.students = sqlite3.connect("db/students.sqlite")
        self.cur1 = self.students.cursor()
        self.y = False
        self.x = False

    def find_some(self):
        self.x = True
        self.some = self.find_line.text()
        if not self.y:
            self.some = self.find_line.text()
            students = sqlite3.connect("db/students.sqlite")
            cur = students.cursor()
            if self.some == '':
                que = '''SELECT * from students'''
                data = cur.execute(que).fetchall()
            else:
                a = self.some.split()
                if len(a) == 1:
                    que = '''SELECT * from students WHERE students.familia = ?'''
                    data = cur.execute(que, (a[0],)).fetchall()
                if len(a) == 2:
                    que = '''SELECT * from students WHERE students.familia = ? and students.name = ?'''
                    data = cur.execute(que, (a[0], a[1])).fetchall()
                if len(a) == 3:
                    que = '''SELECT * from students WHERE students.familia = ? and students.name = ? 
                           and students.father = ?'''
                    data = cur.execute(que, (a[0], a[1], a[3])).fetchall()
                else:
                    que = '''SELECT * from students'''
                    data = cur.execute(que).fetchall()
            self.table_find.setRowCount(len(data))
            self.table_find.setColumnCount(len(data[0]) + 2)

            for i, elem in enumerate(data):
                name = data[i][4] + "->"
                self.btn = QPushButton(name)
                self.btn.setMinimumSize(200, 0)
                self.btn.clicked.connect(self.study)
                self.table_find.setCellWidget(i, 0, self.btn)
                self.btn.setObjectName(data[i][3])
            for j, elem in enumerate(data):
                for i, val in enumerate(elem):
                    self.table_find.setItem(j, i + 2, QTableWidgetItem(val))
        else:
            self.on_activated(self.text)

    def on_activated(self, text):
        self.y = True
        self.text = text

        if text == 'ученик':
            students = sqlite3.connect("db/students.sqlite")
            cur = students.cursor()
            if self.x:

                if self.some == '':
                    que = '''SELECT * from students'''
                    data = cur.execute(que).fetchall()
                else:
                    a = self.some.split()
                    if len(a) == 1:

                        que = '''SELECT * from students WHERE students.familia = ?'''
                        data = cur.execute(que, (a[0],)).fetchall()
                        b = 3
                    elif len(a) == 2:
                        que = '''SELECT * from students WHERE students.familia = ? and students.name = ?'''
                        data = cur.execute(que, (a[0], a[1])).fetchall()
                    elif len(a) == 3:
                        que = '''SELECT * from students WHERE students.familia = ? and students.name = ? 
                               and students.father = ?'''
                        data = cur.execute(que, (a[0], a[1], a[3])).fetchall()
                    else:
                        que = '''SELECT * from students'''
                        data = cur.execute(que).fetchall()
            else:
                que = '''SELECT * from students'''
                data = cur.execute(que).fetchall()

            self.table_find.setRowCount(len(data))
            self.table_find.setColumnCount(len(data[0]) + 2)

            for i, elem in enumerate(data):
                name = data[i][4] + "->"
                self.btn = QPushButton(name)
                self.btn.setMinimumSize(200, 0)
                self.btn.clicked.connect(self.study)
                self.table_find.setCellWidget(i, 0, self.btn)
                self.btn.setObjectName(data[i][3])
            for j, elem in enumerate(data):
                for i, val in enumerate(elem):
                    self.table_find.setItem(j, i + 2, QTableWidgetItem(val))
        if text == "кабинет":
            kab = sqlite3.connect("db/students.sqlite")
            cur = kab.cursor()
            if self.x:
                if self.some == '':
                    que = '''SELECT * from kab'''
                    data = cur.execute(que).fetchall()
                else:

                    que = '''SELECT * from kab WHERE kab.number = ?'''
                    data = cur.execute(que, (self.some,)).fetchall()

            else:
                que = '''SELECT * from kab'''
                data = cur.execute(que).fetchall()

            self.table_find.setRowCount(len(data))
            self.table_find.setColumnCount(2)

            for i, elem in enumerate(data):
                name = data[i][0] + "->"
                self.btn = QPushButton(name)
                self.btn.clicked.connect(self.kabs)
                self.table_find.setCellWidget(i, 0, self.btn)  # (r, c)
                self.btn.setObjectName(data[i][0])
            for j, elem in enumerate(data):
                self.table_find.setItem(j, 1, QTableWidgetItem(elem[0]))
        if text == 'класс':
            students = sqlite3.connect("db/students.sqlite")
            cur = students.cursor()
            if self.x:
                if self.some == '':
                    que = '''SELECT * from students'''
                    data = cur.execute(que).fetchall()
                else:
                    que = '''SELECT * from students WHERE students.class = ?'''
                    data = cur.execute(que, (self.some.upper(),)).fetchall()
            else:
                que = '''SELECT * from students'''
                data = cur.execute(que).fetchall()

            self.table_find.setRowCount(len(data))
            self.table_find.setColumnCount(len(data[0]) + 1)

            for i, elem in enumerate(data):
                name = data[i][3] + "->"
                self.btn = QPushButton(name)
                self.btn.clicked.connect(self.classes)
                self.table_find.setCellWidget(i, 0, self.btn)
                self.btn.setObjectName(data[i][3])
            for j, elem in enumerate(data):
                for i, val in enumerate(elem):
                    self.table_find.setItem(j, i + 1, QTableWidgetItem(val))

    def study(self):
        x = self.sender()
        email = x.text()[:-2]
        students = sqlite3.connect("db/students.sqlite")
        cur = students.cursor()

        que = '''SELECT * from students WHERE students.email = ?'''
        data = cur.execute(que, (email,)).fetchall()

        fio = {}
        f = ['familia', 'name', 'father', 'class', 'email']
        for i in range(len(f)):
            fio[f[i]] = data[0][i]
        self.st = Student(self.teacher_email, fio)
        self.close()
        self.st.show()

    def classes(self):
        x = self.sender()
        num = x.text()[:-2]
        self.kl = Klass(self.teacher_email, num)
        self.close()
        self.kl.show()

    def kabs(self):
        x = self.sender()
        num = x.text()[:-2]
        kabs = sqlite3.connect("db/students.sqlite")
        cur = kabs.cursor()

        que = '''SELECT * from kab WHERE number = ?'''
        data = cur.execute(que, (num,)).fetchall()

        fio = {}
        f = ['number', 'foto']
        for i in range(len(f)):
            fio[f[i]] = 'db/' + data[0][i]
        self.kb = Kabinet(self.teacher_email, fio)
        self.close()
        self.kb.show()
