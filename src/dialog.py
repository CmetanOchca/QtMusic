import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from QtMusic.ui.designdialog import Ui_Dialog
from QtMusic.src.data import Data
from QtMusic.src import bytes_to_pixmap, pixmap_to_bytearray

class DialogWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.song_data = None
        self.setModal(True)
        self.comboBox.addItems(["1", "2", "3", "4", "5"])

        self.lineEdit.setToolTip("Название песни")
        self.lineEdit_2.setToolTip("Имя исполнителя")
        self.timeEdit.setToolTip("Продолжительность песни")
        self.comboBox.setToolTip("Оценка песни")
        self.preview_label.setToolTip("Изображение альбома песни")

        self.PreviewSelection.clicked.connect(self.select_preview)
        self.buttonBox.accepted.connect(self.save_data)
        self.buttonBox.rejected.connect(self._all_clear)
        self.buttonBox.rejected.connect(self.rejected)

    def _set_preview(self, pixmap: QtGui.QPixmap):
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(
                self.preview_label.width(),
                self.preview_label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            self.preview_label.setPixmap(scaled_pixmap)
            self.preview_label.setText("")

    def select_preview(self):
        """
        Выбор файла превью

        :return:
        """
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите превью",
            "",
            "Images (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self._set_preview(QtGui.QPixmap(file_path))

    def save_data(self):
        """
        Сохранение данных в класс Data

        :return:
        """
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit_2.text()) == 0:
            QtWidgets.QMessageBox.warning(self, "Предупреждение", "Необходимо ввести название и исполнителя")
            self._all_clear()
            return
        print('Начало сохранения')
        title = self.lineEdit.text()
        performer = self.lineEdit_2.text()
        duration = self.timeEdit.time().toString('hh:mm')
        assessment = self.comboBox.currentText()
        preview = pixmap_to_bytearray(self.preview_label.pixmap())
        self.song_data = Data()
        self.song_data.update_song_data(
            title,
            performer,
            duration,
            assessment,
            preview
        )
        self._all_clear()
        self.accept()

    def _all_clear(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.timeEdit.setTime(QtCore.QTime(0, 0))
        self.comboBox.setCurrentIndex(0)
        self.preview_label.clear()


    def get_data(self):
        print('Данные успешно переданы в таблицу')
        return self.song_data

    def set_data(self, song_data: Data):
        self.lineEdit.setText(song_data.current_song_data['title'])
        self.lineEdit_2.setText(song_data.current_song_data['performer'])
        duration = song_data.current_song_data['duration'].split(':')
        self.timeEdit.setTime(QtCore.QTime(int(duration[0]),int(duration[1])))
        self.comboBox.setCurrentIndex(int(song_data.current_song_data['assessment']) - 1)
        bytes = song_data.current_song_data["preview"]
        if bytes:
            self._set_preview(bytes_to_pixmap(bytes))
