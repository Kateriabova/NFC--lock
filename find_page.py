from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, QDialog
import sys
from student import Student
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, QDialog, QTableWidget
import sys

class Find(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('find.ui', self)
        self.table_find.cellActivated(row, column)

    def find_some(self):
        fio = {}
        self.st = Student(fio)
        self.fn.close()
        self.find.show()