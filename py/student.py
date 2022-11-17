import traceback

from PyQt5 import uic
from PyQt5.QtWidgets import QPushButton, QMainWindow, \
    QTableWidgetItem, QInputDialog, QMessageBox
import sys
from py.access import Access_1
import sqlite3
import datetime as dt



def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook


class Student(QMainWindow):
    def __init__(self, email_teacher,
                 fio={'familia': 'Рябова', 'name': 'Екатерина', 'father': 'Николевна', 'class': '10В',
                      'email': 'riabovakate@yandex.ru'}):
        super().__init__()
        self.teacher_email = email_teacher
        self.fio = fio #передача информации
        uic.loadUi('ui/student.ui', self)
        self.familia.setText(self.fio['familia'])
        self.name.setText(self.fio['name'])
        self.father.setText(self.fio['father'])
        self.class_2.setText(self.fio['class']) #информация об ученике выводится на экран
        self.back.clicked.connect(self.returning)#кнопка "назад"
        self.familia.setReadOnly(True)
        self.name.setReadOnly(True)
        self.father.setReadOnly(True)
        self.class_2.setReadOnly(True)#информацию нельзя редактировать

        self.give_access.clicked.connect(self.access) #кнопка "дать доступ"

        now = dt.date.today().weekday()
        name_file = 'db/' + str(now) + '.csv' #получение файла с расписанием
        with open(name_file, 'r', encoding='windows-1251') as f:
            classes = f.readline().rstrip().split(';')
            data_2 = [i.rstrip().split(';') for i in f.readlines()]
            key = classes.index(self.fio['class'])
            data = []
            for i in data_2:
                data.append(i[key])
            self.table_lessons.setRowCount(len(data))
            self.table_lessons.setColumnCount(1)
            for i, elem in enumerate(data):
                self.table_lessons.setItem(i, 0, QTableWidgetItem(elem)) #расписание выводится на экран через табличку

        accesses = sqlite3.connect("db/students.sqlite")
        cur2 = accesses.cursor()
        data = cur2.execute("""SELECT * FROM accesses
                            WHERE mail_of_student = ?""", (self.fio['email'],)).fetchall() #поиск кабинетов к которым ученик имеет доступ
        if len(data) != 0:
            self.table_kab.setRowCount(len(data))
            self.table_kab.setColumnCount(len(data[0]))
            for i, elem in enumerate(data):

                for j, val in enumerate(elem):
                    if j != 0:
                        self.table_kab.setItem(i, j - 1, QTableWidgetItem(val))

                    self.btn = QPushButton('ОТМЕНИТЬ  id = ' + str(elem[5]))
                    self.btn.clicked.connect(self.delete)
                    self.table_kab.setCellWidget(i, 5, self.btn)  # (r, c)
                    self.btn.setObjectName('btn' + self.fio['email']) #формирование таблички с кнопками "забрать доступ"
        else:
            self.table_kab.setRowCount(len(data))
            self.table_kab.setColumnCount(0)#нулевая таблица

    def access(self):
        stu = [self.fio['email']]
        self.acs = Access_1(self.teacher_email, stu)
        self.acs.show() #переход на страницу "дать доступ"

    def delete(self): #забрать доступ
        name, ok_pressed = QInputDialog.getText(self, "Подтвердите свои полномочия",
                                                "Введите key") #подтверждения ключом
        accesses = sqlite3.connect("db/students.sqlite")
        cur2 = accesses.cursor()
        x = self.sender()
        em = x.text()[9:].split()[-1]
        data = cur2.execute("""SELECT key FROM accesses WHERE id = ?""", (em,)).fetchall()
        if ok_pressed:
            if name == data[0][0]:
                cur2.execute("""DELETE FROM accesses WHERE id = ?""", (em,)) #если пароль совпал удаление и комит
                accesses.commit()
                accesses = sqlite3.connect("db/students.sqlite")
                cur2 = accesses.cursor()
                data = cur2.execute("""SELECT * FROM accesses
                                            WHERE mail_of_student = ?""", (self.fio['email'],)).fetchall()
                if len(data) != 0:
                    self.table_kab.setRowCount(len(data))
                    self.table_kab.setColumnCount(len(data[0])) #заново формируется таблица доступа, уже без удаленного элемента
                    for i, elem in enumerate(data):

                        for j, val in enumerate(elem):
                            if j != 0:
                                self.table_kab.setItem(i, j - 1, QTableWidgetItem(val))

                            self.btn = QPushButton('ОТМЕНИТЬ  id = ' + str(elem[5]))
                            self.btn.clicked.connect(self.delete)
                            self.table_kab.setCellWidget(i, 5, self.btn)  # (r, c)
                            self.btn.setObjectName('btn' + self.fio['email'])
                else:
                    self.table_kab.setRowCount(len(data))
                    self.table_kab.setColumnCount(0)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("неверный key")
                msg.setWindowTitle("Error")
                msg.exec_() #в случае неверного ключа выводится сообщение об ошибке

    def returning(self): #возврат на страницу поиска
        self.close()

