from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, QDialog
import sys
from access import Access

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook

class Student(QMainWindow):
    def __init__(self, fio={'number': '509', 'foto': '509.jpg'}):
        super().__init__()

        uic.loadUi('student.ui', self)
        self.familia.setText(fio['familia'])
        self.name.setText(fio['name'])
        self.father.setText(fio['father'])
        self.class_2.setText(fio['class'])
        self.right_now.setText(fio['right_now'])
        self.familia.setReadOnly(True)
        self.name.setReadOnly(True)
        self.father.setReadOnly(True)
        self.class_2.setReadOnly(True)
        self.right_now.setReadOnly(True)
        self.give_access.clicked.connect(self.access)

    def access(self):
        self.acs = Access()
        self.acs.show()
