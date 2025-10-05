from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 311)
        MainWindow.setMinimumSize(QtCore.QSize(510, 311))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.central_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.central_layout.setObjectName("central_layout")
        self.central_layout.setContentsMargins(10, 10, 10, 10)
        self.central_layout.setSpacing(10)

        self.search_layout = QtWidgets.QHBoxLayout()
        self.search_layout.setObjectName("search_layout")

        self.search_line = QtWidgets.QLineEdit(self.centralwidget)
        self.search_line.setText("")
        self.search_line.setMaxLength(32700)
        self.search_line.setClearButtonEnabled(True)
        self.search_line.setObjectName("search_line")
        self.search_layout.addWidget(self.search_line)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.search_layout.addItem(spacerItem)

        self.central_layout.addLayout(self.search_layout)

        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.main_layout.setSpacing(10)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels([
            "Превью",
            "Название песни",
            "Исполнитель",
            "Время"
        ])

        header = self.tableWidget.horizontalHeader()

        self.tableWidget.setColumnWidth(0, 80)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)

        self.tableWidget.setColumnWidth(1, 120)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.tableWidget.setColumnWidth(2, 100)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.tableWidget.setColumnWidth(3, 80)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)

        self.main_layout.addWidget(self.tableWidget)

        self.buttons_container = QtWidgets.QWidget(self.centralwidget)
        self.buttons_container.setObjectName("buttons_container")
        self.buttons_container.setMaximumWidth(150)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.buttons_container)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")

        self.Create = QtWidgets.QPushButton(self.buttons_container)
        self.Create.setMinimumSize(QtCore.QSize(0, 35))
        self.Create.setObjectName("Create")
        self.verticalLayout.addWidget(self.Create)

        self.Edit = QtWidgets.QPushButton(self.buttons_container)
        self.Edit.setEnabled(False)
        self.Edit.setMinimumSize(QtCore.QSize(0, 35))
        self.Edit.setCheckable(False)
        self.Edit.setAutoExclusive(False)
        self.Edit.setAutoDefault(False)
        self.Edit.setDefault(False)
        self.Edit.setFlat(False)
        self.Edit.setObjectName("Edit")
        self.verticalLayout.addWidget(self.Edit)

        self.Save = QtWidgets.QPushButton(self.buttons_container)
        self.Save.setMinimumSize(QtCore.QSize(0, 35))
        self.Save.setObjectName("Save")
        self.verticalLayout.addWidget(self.Save)

        self.verticalLayout.addStretch(1)

        self.main_layout.addWidget(self.buttons_container)

        self.main_layout.setStretch(0, 4)
        self.main_layout.setStretch(1, 1)

        self.central_layout.addLayout(self.main_layout)

        self.central_layout.setStretch(1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(False)
        self.Create.setText(_translate("MainWindow", "Создать"))
        self.Edit.setText(_translate("MainWindow", "Редактировать"))
        self.Save.setText(_translate("MainWindow", "Сохранить"))
        self.search_line.setPlaceholderText(_translate("MainWindow", "Поиск..."))