from PyQt5 import QtCore,QtGui,QtWidgets

def bytes_to_pixmap(bytes):
    ba = QtCore.QByteArray(bytes)
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(ba, "PNG")
    return pixmap

def pixmap_to_bytearray(pixmap):
    if not pixmap:
        return None
    ba = QtCore.QByteArray()
    buff = QtCore.QBuffer(ba)
    buff.open(QtCore.QIODevice.WriteOnly)
    pixmap.save(buff, "PNG")
    return ba.data()