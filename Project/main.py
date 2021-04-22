from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication
import sys
import os
import application

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    w = application.MainWindow()
    w.show()
    sys.exit(app.exec_())



