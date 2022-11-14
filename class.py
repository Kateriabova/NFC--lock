from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, QDialog, QTableWidgetItem
import sys
from access import Access
from PyQt5.QtGui import QPixmap
import traceback
import sqlite3
import datetime as dt
from student import Student



def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook

class Klass(QMainWindow):
    def __init__(self, teacher_email, number):
        super().__init__()
        self.teacher_email = teacher_email
        self.num = number
        uic.loadUi('class.ui', self)
        self.name.setText(self.name)

        now = dt.date.today().weekday()
        name_file = 'db/' + str(now) + '.csv'
        with open(name_file, 'r', encoding='windows-1251') as f:
            classes = f.readline().rstrip().split(';')
            data_2 = [i.rstrip().split(';') for i in f.readlines()]
            key = classes.index(self.fio['class'])
            data = []
            for i in data_2:
                data.append(i[key])
            self.table_lessons.setRowCount(len(data))
            self.table_lessons.setColumnCount(1)
            for i, elem in enumerate(data):
                self.table_lessons.setItem(0, 1, QTableWidgetItem(elem))
        students = sqlite3.connect("db/students.sqlite")
        cur2 = students.cursor()
        data = cur2.execute("""SELECT * FROM students
                                    WHERE class = ?""", (self.num,)).fetchall()
        self.table_class.setRowCount(len(data))
        self.table_class.setColumnCount(2)
        for i, elem in enumerate(data):
            self.table_lesson.setItem(i, 1, QTableWidgetItem(elem[0]))
            self.btn = QPushButton(elem[4] + '->')
            self.btn.clicked.connect(self.study)
            self.table.setCellWidget(i, 0, self.btn)  # (r, c)
            self.btn.setObjectName('btn' + elem[4])


    def access(self):
        stu = []
        self.acs = Access(self.teacher_email, stu)
        self.acs.show()

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
