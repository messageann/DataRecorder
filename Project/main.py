from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
import sys
import application


if __name__ == '__main__':
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    w = application.MainWindow()
    w.show()
    sys.exit(app.exec_())
