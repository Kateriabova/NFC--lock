import traceback

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, \
    QDialog, QInputDialog
import sys
from find_page import Find
import sqlite3 as sq
import traceback


class Entrence(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/registration.ui', self)
        self.enter.clicked.connect(self.good_entrance)
        self.password_new.clicked.connect(self.pas)

    def good_entrance(self):
        password = self.password.text()
        email_1 = self.email.text()

        a = sq.connect('db/teachers_1.sqlite')
        b = a.cursor()

        c = b.execute("""SELECT password FROM teachers
                    WHERE email = ?""", (email_1,)).fetchall()
        for i in c:
            if i[0] == password:
                self.fn = Find(email_1)
                en.close()
                self.fn.show()
            else:
                self.enter.setText('Скорее всего, неверный пароль')
        if len(c) == 0:
            self.enter.setText('Скорее всего, неверная почта')

    def pas(self):
        name, ok_pressed = QInputDialog.getText(self, "Смена пароля",
                                                "Введите почту")
        if ok_pressed:
            self.password_new.setText('заявка отправлена')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    en = Entrence()
    en.show()
    sys.exit(app.exec())
