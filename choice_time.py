from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, QDialog
import sys

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook

class Time(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('time.ui', self)
        c = [self.c0, self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8]
        self.numbers = []
        self.ok.clicked.connect(self.ret)
        for i in c:
            i.clicked.connect(self.lesson)

    def ret(self):
        self.close()

    def lesson(self):
        x = self.sender()
        self.numbers.append(int(x.text()[1]) + 1)

