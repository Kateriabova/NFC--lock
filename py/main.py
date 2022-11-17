from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QInputDialog, QMessageBox, QTableWidgetItem
import sys

import traceback

from py.find_page import Find
import sys
import sqlite3

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


class Entrence(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/registration.ui', self)
        self.enter.clicked.connect(self.good_entrance)
        self.password_new.clicked.connect(self.pas) #подключение уика, кнопок входа и "забыл пароль"

    def good_entrance(self):
        password = self.password.text()
        email_1 = self.email.text() #пользователь ввел пароль и логин

        a = sqlite3.connect('db/students.sqlite')
        b = a.cursor()

        c = b.execute("""SELECT password FROM teachers
                    WHERE email = ?""", (email_1,)).fetchall() #поиск логина в базе данных
        for i in c:
            if i[0] == password: #проверка на сопоставление логина и пароля

                self.fn = Find(email_1)
                self.close()
                self.fn.show() #переход на новую страницу поиска
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("скорее всего, неверный пароль")
                msg.setWindowTitle("Error")
                msg.exec_() #сообщение об ошибке, если пароль не совпал
        if len(c) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("скорее всего, неверная почта")
            msg.setWindowTitle("Error")
            msg.exec_() #сообщение об ошибке, если логина нет в базе данных

    def pas(self):
        name, ok_pressed = QInputDialog.getText(self, "Смена пароля",
                                                "Введите почту")
        if ok_pressed:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("заявка отправлена!")
            msg.setWindowTitle("waiting now")
            msg.exec_() #сообщение об отправлении заявки


if __name__ == '__main__':
    app = QApplication(sys.argv)
    en = Entrence()
    en.show()
    sys.exit(app.exec())
