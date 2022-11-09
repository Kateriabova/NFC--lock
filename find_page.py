from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, QDialog
import sys
from student import Student
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, QDialog, QTableWidget
import sys
import sqlite3

class Find(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('find.ui', self)
        self.table_find.cellActivated(row, column)
        self.students = sqlite3.connect("students.sqlite")
        self.cur1 = self.students.cursor()

    def find_some(self):
        fio = {}
        self.st = Student(fio)
        self.fn.close()
        self.find.show()