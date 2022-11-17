import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, \
    QDialog, QTableWidgetItem
import sys

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook

class Stu(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/student_choice.ui', self)
        kab = sqlite3.connect("db/students.sqlite")
        cur = kab.cursor()
        que = '''SELECT * from students''' #формирование таблицы поиска table_student
        data = cur.execute(que).fetchall()
        self.table_student.setRowCount(len(data))
        self.table_student.setColumnCount(4)

        for i, elem in enumerate(data):
            name = data[i][0]
            self.btn = QPushButton(name)
            self.btn.clicked.connect(self.puding) #дать доступ новому ученику
            self.table_student.setCellWidget(i, 0, self.btn)  # (r, c)
            self.btn.setObjectName(data[i][4]) #кнопочка в таблице
        for j, elem in enumerate(data):
            self.table_student.setItem(j, 1, QTableWidgetItem(elem[0]))
            self.table_student.setItem(j, 2, QTableWidgetItem(elem[1])) #заполнение таблицы фамилией-именем

        self.ok.clicked.connect(self.ret) #нажатие на кнопку ок
    def puding(self):
        x = self.sender().text() #email
        with open('db/login_student.txt', 'w') as f:
            pass
        with open('db/login_student.txt', 'w') as f:
            print(x, file=f) #очистили файл для записи и записали логин ученика

    def ret(self):
        self.close() #закрыли окошко