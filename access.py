from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, QDialog
import sys
from choice_kab import Kab
from choice_time import Time

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook

class Access(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('choice_form.ui', self)
        self.time.clicked.connect(self.choice_time)
        self.kab.clicked.connect(self.choice_kab)
    """def ret(self):
        self.close()"""

    def choice_time(self):
        self.tm = Time()
        self.tm.show()

    def choice_kab(self):
        self.kb = Kab()
        self.kb.show()
