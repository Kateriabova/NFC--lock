from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox, QMainWindow, \
    QDialog, QTableWidgetItem, QInputDialog
import sys
from access import Access_2
from PyQt5.QtGui import QPixmap
import traceback
import sqlite3


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
        self.number.setText(information['number'][3:])
        self.number.setReadOnly(True)

        self.label = QLabel('1234567890')
        self.label.setMaximumSize(200, 300)
        file = Image.open(information['foto'])

        pixmap = QPixmap(information['foto']).scaled(200, 300)
        self.label.setPixmap(pixmap)
        self.horizontalLayout.addWidget(self.label)

        accesses = sqlite3.connect("db/accesess.sqlite")
        cur2 = accesses.cursor()
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
                self.btn.setObjectName('btn' + str(elem[5]))
        else:
            self.table.setRowCount(len(data))
            self.table.setColumnCount(0)

    def access(self):
        self.acs = Access_2(self.teacher_email, self.information['number'])
        self.acs.show()

    def delete(self):
        name, ok_pressed = QInputDialog.getText(self, "Подтвердите свои полномочия",
                                                "Введите key")
        accesses = sqlite3.connect("db/accesess.sqlite")
        cur2 = accesses.cursor()
        x = self.sender()
        em = x.text()[9:].split()[-1]
        data = cur2.execute("""SELECT key FROM accesses WHERE id = ?""", (em,)).fetchall()
        if ok_pressed:

            if name == data[0][0]:
                cur2.execute("""DELETE FROM accesses WHERE id = ?""", (em,))
                accesses.commit()
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
                        self.btn.setObjectName('btn' + str(elem[5]))
                else:
                    self.table.setRowCount(len(data))
                    self.table.setColumnCount(0)