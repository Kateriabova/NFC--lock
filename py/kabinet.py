from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QPushButton, QLabel, QMainWindow, \
    QTableWidgetItem, QInputDialog
import sys
from py.access import Access_2
from PyQt5.QtGui import QPixmap
import traceback
import sqlite3
from py.find_page import Find


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook


class Kabinet(QMainWindow):
    def __init__(self, teacher_email, information={'number': '509', 'foto': 'db/509.png'}):
        super().__init__()
        self.information = information
        self.teacher_email = teacher_email
        uic.loadUi('ui/kab.ui', self)
        self.number.setText(information['number'][3:])#подключение к уику, размещение на странице информации
        self.number.setReadOnly(True)
        self.back.clicked.connect(self.returning)#кнопка назад
        self.label = QLabel('1234567890')
        self.label.setMaximumSize(200, 300) #лейбл для картинки
        file = Image.open(information['foto']) #картинка

        pixmap = QPixmap(information['foto']).scaled(200, 300)
        self.label.setPixmap(pixmap)
        self.horizontalLayout.addWidget(self.label) #вставляем картинку

        accesses = sqlite3.connect("../db/students.sqlite")
        cur2 = accesses.cursor()
        data = cur2.execute("""SELECT * FROM accesses
                                    WHERE kab = ?""", (self.information['number'],)).fetchall() #список учеников, у которых есть доступ в этот кабинет

        if len(data) != 0: #если они есть, мы их вставляем в табличку
            self.table.setRowCount(len(data))
            self.table.setColumnCount(len(data[0]) - 2)
            for i, elem in enumerate(data):

                for j, val in enumerate(elem):
                    if j != 5 and j != 6 and j != 1:
                        if j == 0:
                            self.table.setItem(i, j, QTableWidgetItem(val))
                        else:
                            self.table.setItem(i, j - 1, QTableWidgetItem(val))

                self.btn = QPushButton('ОТМЕНИТЬ id = ' + str(elem[5]))
                self.btn.clicked.connect(self.delete)
                self.table.setCellWidget(i, 4, self.btn)  # (r, c)
                self.btn.setObjectName('btn' + str(elem[5])) #и вставляем кнопку "забрать доступ"
        else:
            self.table.setRowCount(len(data))
            self.table.setColumnCount(0) #если нет учеников, то таблица нулевая

    def access(self): #переход на страницу доступа
        self.acs = Access_2(self.teacher_email, self.information['number'])
        self.acs.show()

    def delete(self): #удаление доступа
        name, ok_pressed = QInputDialog.getText(self, "Подтвердите свои полномочия",
                                                "Введите key") #сообщение, куда ввести ключ
        accesses = sqlite3.connect("../db/students.sqlite")
        cur2 = accesses.cursor()
        x = self.sender()
        em = x.text()[9:].split()[-1] #id удаляемого элемента
        data = cur2.execute("""SELECT key FROM accesses WHERE id = ?""", (em,)).fetchall() #нашли элемент в бд
        if ok_pressed:

            if name == data[0][0]: #если ключ подошел
                cur2.execute("""DELETE FROM accesses WHERE id = ?""", (em,))
                accesses.commit() #удаление и комит
                data = cur2.execute("""SELECT * FROM accesses
                                                    WHERE kab = ?""", (self.information['number'],)).fetchall()

                if len(data) != 0:
                    self.table.setRowCount(len(data))
                    self.table.setColumnCount(len(data[0]) - 2)
                    for i, elem in enumerate(data):

                        for j, val in enumerate(elem):
                            if j != 5 and j != 6 and j != 1:
                                if j == 0:
                                    self.table.setItem(i, j, QTableWidgetItem(val))
                                else:
                                    self.table.setItem(i, j - 1, QTableWidgetItem(val))

                        self.btn = QPushButton('ОТМЕНИТЬ id = ' + str(elem[5]))
                        self.btn.clicked.connect(self.delete)
                        self.table.setCellWidget(i, 4, self.btn)  # (r, c)
                        self.btn.setObjectName('btn' + str(elem[5])) #заново формируется table widget с обновленной информацией
                else:
                    self.table.setRowCount(len(data))
                    self.table.setColumnCount(0)

    def returning(self): #возврат на страницу поиска
        self.fn = Find(self.teacher_email)
        self.close()
        self.fn.show()