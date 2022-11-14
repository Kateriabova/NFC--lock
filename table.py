class TeacherAddPupil(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('teacher_add_class.ui', self)
        self.show()
        self.pushButton.clicked.connect(self.clickBtn)
        self.pushButton_2.clicked.connect(self.openFile)

    def clickBtn(self):
        print(1)
        self.openTeacherEntrance()

    def openTeacherEntrance(self):
        self.hide()
        self.a = TeacherEntrance()

    def openFile(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file')[0]
        if self.fname:
            f = open(self.fname, 'r', encoding='utf-8')
            with f:
                data = [i.rstrip() for i in f.readlines()]

                self.tableWidget.setRowCount(len(data))
                self.tableWidget.setColumnCount(4)
                self.titles = data[0].split(';')
                for i, elem in enumerate(data):
                    for j, val in enumerate(elem.split(';')):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(val))

self.Btn = QtWidgets.QPushButton(self.centralwidget)
 self.Btn.setGeometry(QtCore.QRect(500, 10, 90, 30))
 self.Btn.setObjectName("Btn")

 self.tableWidget.setItem(1, 0, QTableWidgetItem('Текст'))
 self.tableWidget.setItem(2, 0, QTableWidgetItem('Текст1'))
 self.tableWidget.setItem(3, 0, QTableWidgetItem(self.Btn.clicked.connect(self.LoadData)))