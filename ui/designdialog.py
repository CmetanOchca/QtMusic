from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(359, 257)
        Dialog.setMinimumSize(QtCore.QSize(359, 257))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 220, 174, 34))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.PreviewSelection = QtWidgets.QPushButton(Dialog)
        self.PreviewSelection.setGeometry(QtCore.QRect(190, 10, 123, 34))
        self.PreviewSelection.setObjectName("PreviewSelection")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(190, 50, 123, 121))
        self.widget.setObjectName("widget")
        self.preview_label = QtWidgets.QLabel(self.widget)
        self.preview_label.setGeometry(0, 0, self.widget.width(), self.widget.height())

        # Настраиваем внешний вид
        self.preview_label.setStyleSheet("""
                    QLabel {
                        border: 1px solid #cccccc;
                        background-color: #f0f0f0;
                    }
                """)
        self.preview_label.setText("Превью\nне выбрано")
        self.preview_label.setWordWrap(True)

        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 138, 244))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleSong = QtWidgets.QLabel(self.layoutWidget)
        self.TitleSong.setObjectName("TitleSong")
        self.verticalLayout.addWidget(self.TitleSong)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.Performer = QtWidgets.QLabel(self.layoutWidget)
        self.Performer.setObjectName("Performer")
        self.verticalLayout.addWidget(self.Performer)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.Duration = QtWidgets.QLabel(self.layoutWidget)
        self.Duration.setObjectName("Duration")
        self.verticalLayout.addWidget(self.Duration)
        self.timeEdit = QtWidgets.QTimeEdit(self.layoutWidget)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.Assessment = QtWidgets.QLabel(self.layoutWidget)
        self.Assessment.setObjectName("Assessment")
        self.verticalLayout.addWidget(self.Assessment)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.PreviewSelection.setText(_translate("Dialog", "Выбрать превью"))
        self.TitleSong.setText(_translate("Dialog", "Название*:"))
        self.Performer.setText(_translate("Dialog", "Исполнитель*:"))
        self.Duration.setText(_translate("Dialog", "Продолжительность:"))
        self.Assessment.setText(_translate("Dialog", "Оценка:"))


