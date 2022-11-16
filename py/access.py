import sqlite3
import traceback

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, \
    QDialog, QMessageBox
import sys
from choice_kab import Kab
from choice_time import Time
from random import random

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook

class Access_1(QDialog): #класс первый, с кнопками "выбрать время" и "выбрать кабинет"
    def __init__(self, teacher_email, stu):
        super().__init__()
        self.stu = stu
        self.teacher_email = teacher_email
        uic.loadUi('ui/choice_form.ui', self)
        self.time1.clicked.connect(self.choice_time) #кнопка выбрать время
        self.kab.clicked.connect(self.choice_kab) #кнопка выбрать кабинет
        self.access.clicked.connect(self.ret) #кнопка дать доступ

    def ret(self): #дать доступ (передача в бд и закрытие диалога)

        with open('../db/number_kab.txt', 'r') as f: #здесь записан номер выбранного кабинета
            kab = f.readline().strip()
            le = sqlite3.connect("../db/students.sqlite")
            cur2 = le.cursor()
            a = int(cur2.execute('''SELECT * from accesses''').fetchall()[-1][-2]) + 1 #последний id в таблице доступа
            times = sqlite3.connect("../db/students.sqlite")
            cur = times.cursor()
            que = '''SELECT * from ti''' #открытие таблицы, где записаны пары времени, начала и конца, на которое дать доступ
            data = cur.execute(que, ).fetchall()
            for i in self.stu: #список учеников
                for j in data: #временные пары
                    k = str(int(random() * 1000)) #key доступа
                    information = (i, kab, self.teacher_email, j[0], j[1], a, k) #информация доступа: ученик, кабинет, логин учителя, ырем яначала, время конца и ключ
                    cur2.execute("INSERT INTO accesses (mail_of_student, kab, mail_of_teacher, data_since, data_before, id, key) VALUES(?, ?, ?, ?, ?, ?, ?)", information)
                    le.commit() #добавление и комит
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("успешно добавлено!")
                    msg.setWindowTitle(f"id: {a}, key = {k}")
                    msg.exec_()  # сообщение об успешном добавлении и вывод ключа
            self.close()

    def choice_time(self): #переход к диалогу выбрать время
        self.tm = Time()
        self.tm.show()


    def choice_kab(self): #переход к диалогу выбрать кабинет
        self.kb = Kab()
        self.kb.show()

class Access_2(QDialog): #класс второй с кнопками "выбрать время" и "выбрать ученика"
    def __init__(self, teacher_email, num):
        super().__init__()
        self.kab = num
        self.teacher_email = teacher_email
        uic.loadUi('ui/choice_form_2.ui', self)
        self.time.clicked.connect(self.choice_time) #кнопка выбрать время
        self.student.clicked.connect(self.choice_student) #кнопка выбрать ученика
        self.access.clicked.connect(self.ret)

    def ret(self): #передача информации в базу данных и закрытие окна
        with open('../db/login_student.txt', 'r') as f:  # здесь записан логин ученика выбранного кабинета
            stu = f.readline().strip()
            le = sqlite3.connect("../db/students.sqlite")
            cur2 = le.cursor()
            a = int(cur2.execute('''SELECT * from accesses''').fetchall()[-1][-2]) + 1  # последний id в таблице доступа
            times = sqlite3.connect("../db/students.sqlite")
            cur = times.cursor()
            que = '''SELECT * from ti'''  # открытие таблицы, где записаны пары времени, начала и конца, на которое дать доступ
            data = cur.execute(que, ).fetchall()
            for j in data:  # временные пары
                k = str(int(random() * 1000))  # key доступа
                information = (stu, self.kab, self.teacher_email, j[0], j[1], a, k)  # информация доступа: ученик, кабинет, логин учителя, ырем яначала, время конца и ключ
                cur2.execute(
                    "INSERT INTO accesses (mail_of_student, kab, mail_of_teacher, data_since, data_before, id, key) VALUES(?, ?, ?, ?, ?, ?, ?)",
                    information)
                le.commit()  # добавление и комит
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("успешно добавлено!")
                msg.setWindowTitle(f"id: {a}, key = {k}")
                msg.exec_()  # сообщение об успешном добавлении и вывод ключа
            self.close()

    def choice_time(self): #переход к выбору времени
        self.tm = Time()
        self.tm.show()

    def choice_student(self): #переход к выбору ученика
        self.st = St()
        self.st.show()
