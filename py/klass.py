from PyQt5 import uic
from PyQt5.QtWidgets import QPushButton, QMainWindow, QTableWidgetItem
import sys
from access import Access_1
import traceback
import sqlite3
import datetime as dt
from py.student import Student




def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook

class Klass(QMainWindow):
    def __init__(self, teacher_email, number):
        super().__init__()
        self.teacher_email = teacher_email
        self.num = number
        uic.loadUi('ui/class.ui', self)
        self.name.setText(self.num)
        self.name.setReadOnly(True)#инициализация, подключение уика, размещение информации на странице
        self.back.clicked.connect(self.returning)  # кнопка назад
        now = dt.date.today().weekday()
        name_file = 'db/' + str(now) + '.csv' #файл с расписанием
        with open(name_file, 'r', encoding='windows-1251') as f:
            classes = f.readline().rstrip().split(';')
            data_2 = [i.rstrip().split(';') for i in f.readlines()]
            key = classes.index(self.num)
            data = []
            for i in data_2:
                data.append(i[key])
            self.table_lessons.setRowCount(len(data))
            self.table_lessons.setColumnCount(1)
            for i, elem in enumerate(data):
                self.table_lessons.setItem(i, 0, QTableWidgetItem(elem)) #размещение распаисания
        students = sqlite3.connect("db/students.sqlite")
        cur2 = students.cursor()
        data = cur2.execute("""SELECT * FROM students
                                    WHERE class = ?""", (self.num,)).fetchall() #список учеников в этом классе
        self.table_class.setRowCount(len(data))
        self.table_class.setColumnCount(2)
        for i, elem in enumerate(data):
            self.table_class.setItem(i, 1, QTableWidgetItem(elem[0]))
            self.btn = QPushButton(elem[4] + '->')
            self.btn.clicked.connect(self.study) #кнопка перехода на конкретного ученика
            self.table_class.setCellWidget(i, 0, self.btn)  # (r, c)
            self.btn.setObjectName('btn' + elem[4]) #информация об учениках класса в table widget
        self.give_acces.clicked.connect(self.access)

    def access(self): #дать доступ
        stu = []
        students = sqlite3.connect("db/students.sqlite")
        cur2 = students.cursor()
        data = cur2.execute("""SELECT * FROM students
                                            WHERE class = ?""", (self.num,)).fetchall()  # список учеников в этом классе
        for i in data:
            stu.append(i[4]) #список логинов учеников
        self.acs = Access_1(self.teacher_email, stu) #переход на страницу доступа
        self.acs.show()

    def study(self): #перейти к опр. ученику
        x = self.sender()
        email = x.text()[:-2] #логин ученика
        students = sqlite3.connect("db/students.sqlite")
        cur = students.cursor()

        que = '''SELECT * from students WHERE students.email = ?'''
        data = cur.execute(que, (email,)).fetchall() #поиск

        fio = {}
        f = ['familia', 'name', 'father', 'class', 'email']
        for i in range(len(f)):
            fio[f[i]] = data[0][i] #формирование данных
        self.st = Student(self.teacher_email, fio)
        self.close() #переход на страницу студента
        self.st.show()

    def returning(self): #возврат на страницу поиска
        self.close()
