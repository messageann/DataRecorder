from PyQt5.QtWidgets import QApplication
import sys
import application

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = application.MainWindow()
    w.show()
    sys.exit(app.exec_())
