import os
import sys
from PyQt5 import QtWidgets
from src.mainwindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    M_window = MainWindow()
    M_window.show()
    app.exec_()
