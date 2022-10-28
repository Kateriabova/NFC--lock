from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox
import sys


class Entrence(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Авторизация')
        self.setGeometry(100, 100, 1500, 900)

        self.str_1 = QLineEdit('введите логин:', self)
        self.str_2 = QLineEdit('введите пароль:', self)


        self.str_1.move(650, 200)
        self.str_1.resize(200, 40)
        self.str_2.move(650, 270)
        self.str_2.resize(200, 40)

        self.capital = QLabel('Авторизуйтесь', self)
        self.capital.move(710, 100)
        self.capital.resize(100, 50)

        self.entr = QPushButton('войти', self)
        self.entr.move(700, 350)
        self.entr.resize(100, 50)
        self.entr.clicked.connect(self.good_entrence)

    def good_entrence(self):
        print('qu')
        self.main = Mainer()
        en.close()
        self.main.show()




class Mainer(QWidget):
    def __init__(self):
        super().__init__()
        print('Hello')
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Главная страница')
        self.setGeometry(100, 100, 1500, 900)

        self.capital = QLabel('Я солнышко:)', self)
        self.capital.move(710, 100)
        self.capital.resize(100, 50)

        self.jbt = QPushButton('just_a_button', self)
        self.jbt.move(700, 350)
        self.jbt.resize(100, 50)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    en = Entrence()
    en.show()
    sys.exit(app.exec())