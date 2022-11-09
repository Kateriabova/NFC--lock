from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, QDialog
import sys
from find_page import Find



def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)

sys.excepthook = excepthook

class Entrence(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('registration.ui', self)
        self.enter.clicked.connect(self.good_entrence)

    def good_entrence(self):
        self.fn = Find()
        en.close()
        self.fn.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    en = Entrence()
    en.show()
    sys.exit(app.exec())