import sys
import os
import json
import base64
from pathlib import Path

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QPixmap

from ui.designmainwindow import Ui_MainWindow
from src.dialog import DialogWindow
from src.data import Data
from src import bytes_to_pixmap


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.all_data = list()
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.search_line.textChanged.connect(self.filter_table)

        self.Create.clicked.connect(self.open_dialog)
        self.dialog = DialogWindow()
        self.Edit.clicked.connect(self.redact)
        self.Save.clicked.connect(self.save_data)

        self.tableWidget.itemSelectionChanged.connect(self.change_edit_button)

        self.dialog.buttonBox.accepted.connect(self.update_table)
        if self.read_data():
            self.update_table()

    def save_data(self):
        if len(self.all_data) == 0:
            return
        with open('info.json', 'w', encoding='utf-8') as file:
            for data in self.all_data:
                current_item = data.current_song_data
                item_data = {
                    "title": current_item["title"],
                    "performer": current_item["performer"],
                    "duration": current_item["duration"],
                    "assessment": current_item["assessment"],
                    "preview": base64.b64encode(current_item["preview"]).decode('utf-8')
                    if current_item["preview"] else None
                }
                file.write(json.dumps(item_data) + '\n')

    def read_data(self):
        if not Path('info.json').exists():
            return False
        with open('info.json', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                item_data = json.loads(line)
                preview = base64.b64decode(item_data["preview"]) if item_data["preview"] else b""

                song_data = Data()
                song_data.update_song_data(
                    item_data["title"],
                    item_data["performer"],
                    item_data["duration"],
                    item_data["assessment"],
                    preview
                )
                self.all_data.append(song_data)
            return True
        return False

    def open_dialog(self):
        self.dialog.raise_()
        self.dialog.show()

    def filter_table(self, text):
        """
        Фильтрация таблицы QTableWidget по введенному тексту

        :param text:
        :return:
        """
        text_lower = text.lower()

        for row in range(self.tableWidget.rowCount()):
            row_hidden = True

            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item and text_lower in item.text().lower():
                    row_hidden = False
                    break

            self.tableWidget.setRowHidden(row, row_hidden)

    def redact(self):
        row = self.tableWidget.selectedItems()[0].row()
        self.dialog.set_data(self.all_data[row])
        self.open_dialog()

    def update_table(self):
        song_data = self.dialog.get_data()
        if len(self.tableWidget.selectedItems()) > 0:
            index = self.tableWidget.selectedItems()[0].row()
            self.all_data.pop(index)
            self.all_data.insert(index, song_data)
        if not self.all_data.__contains__(song_data) and song_data is not None:
            self.all_data.append(song_data)
        self.tableWidget.setRowCount(0)
        for item in self.all_data:
            current_data = item.current_song_data
            row_position = self.tableWidget.rowCount()

            self.tableWidget.insertRow(row_position)

            if current_data["preview"]:
                pixmap = bytes_to_pixmap(current_data["preview"])
                scaled_pixmap = pixmap.scaled(80, 80, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                preview_label = QtWidgets.QLabel()
                preview_label.setPixmap(scaled_pixmap)
                preview_label.setAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setCellWidget(row_position, 0, preview_label)
            else:
                self.tableWidget.setItem(row_position, 0, QTableWidgetItem("Нет изображения"))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(current_data["title"]))

            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(current_data["performer"]))

            self.tableWidget.setItem(row_position, 3, QTableWidgetItem(current_data["duration"]))

        self.tableWidget.resizeRowsToContents()

    def change_edit_button(self):
        if len(self.tableWidget.selectedItems())>0:
            self.Edit.setEnabled(True)
        else:
            self.Edit.setEnabled(False)
