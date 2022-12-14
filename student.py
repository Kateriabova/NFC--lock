from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, QDialog
import sys
from access import Access
import sqlite3
import datetime as dt

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook

class Student(QMainWindow):
    def __init__(self, fio={'familia': 'Рябова', 'name': 'Екатерина', 'father': 'Николевна', 'class': '10В'}):
        super().__init__()

        uic.loadUi('student.ui', self)
        self.familia.setText(fio['familia'])
        self.name.setText(fio['name'])
        self.father.setText(fio['father'])
        self.class_2.setText(fio['class'])

        self.familia.setReadOnly(True)
        self.name.setReadOnly(True)
        self.father.setReadOnly(True)
        self.class_2.setReadOnly(True)


        now = dt.date.today()
        with open('')
        self.give_access.clicked.connect(self.access)

    def access(self):
        self.acs = Access()
        self.acs.show()
