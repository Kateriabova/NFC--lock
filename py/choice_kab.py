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

class Kab(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/kab_choice.ui', self)
        kab = sqlite3.connect("../db/students.sqlite")
        cur = kab.cursor()
        que = '''SELECT * from kab'''
        data = cur.execute(que).fetchall()
        self.table_find.setRowCount(len(data)) #создание таблицы кабинетов table_find
        self.table_find.setColumnCount(2)

        for i, elem in enumerate(data):
            name = data[i][0] + "->"
            self.btn = QPushButton(name)
            self.btn.clicked.connect(self.kabs)
            self.table_find.setCellWidget(i, 0, self.btn)  # (r, c)
            self.btn.setObjectName(data[i][0]) #кнопочка с ссылкой на кабинет
        for j, elem in enumerate(data):
            self.table_find.setItem(j, 1, QTableWidgetItem(elem[0])) #табличка кабинетов
        self.ok.clicked.connect(self.ret) #нажатие на кнопку ок
    def kabs(self): #выбрали кабинет
        x = self.sender().text()[:-2]
        with open('../db/number_kab.txt', 'w') as f:
            pass
        with open('../db/number_kab.txt', 'w') as f:
            print(x, file=f) #записали его в файл

    def ret(self):
        self.close() #закрыли окно