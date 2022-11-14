import sqlite3
import traceback

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, QDialog
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

class Access_1(QDialog):
    def __init__(self, teacher_email, stu):
        super().__init__()
        self.stu = stu
        self.teacher_email = teacher_email
        uic.loadUi('ui/choice_form.ui', self)
        self.time1.clicked.connect(self.choice_time)
        self.kab.clicked.connect(self.choice_kab)
        self.access.clicked.connect(self.ret)

    def ret(self):

        with open('db/number_kab.txt', 'r') as f:
            kab = f.readline().strip()
            le = sqlite3.connect("db/accesess.sqlite")
            cur2 = le.cursor()
            a = int(cur2.execute('''SELECT * from accesses''').fetchall()[-1][-2]) + 1
            times = sqlite3.connect("db/lessons.sqlite")
            cur = times.cursor()
            que = '''SELECT * from ti'''
            data = cur.execute(que, ).fetchall()
            for i in self.stu:
                for j in data:
                    information = (i, kab, self.teacher_email, j[0], j[1], a, str(int(random() * 1000)))
                    cur2.execute("INSERT INTO accesses (mail_of_student, kab, mail_of_teacher, data_since, data_before, id, key) VALUES(?, ?, ?, ?, ?, ?, ?)", information)
                    le.commit()
            self.close()

    def choice_time(self):
        self.tm = Time()
        self.tm.show()


    def choice_kab(self):
        self.kb = Kab()
        self.kb.show()

class Access_2(QDialog):
    def __init__(self, teacher_email, num):
        super().__init__()
        self.kab = num
        self.teacher_email = teacher_email
        uic.loadUi('ui/choice_form_2.ui', self)

        self.student.clicked.connect(self.choice_kab)
        self.access.clicked.connect(self.ret)

    def ret(self):
        self.close()

    def choice_time(self):
        self.tm = Time()
        self.tm.show()

    def choice_kab(self):
        self.kb = Kab()
        self.kb.show()