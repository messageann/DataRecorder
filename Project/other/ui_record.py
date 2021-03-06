# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_record.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 690)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("background-color:#EEEEEE;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1051, 671))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")

        self.scripts = QtWidgets.QWidget()
        self.scripts.setStyleSheet("")
        self.scripts.setObjectName("scripts")
        self.tabWidget.addTab(self.scripts, "")
        self.rec = QtWidgets.QWidget()
        self.rec.setObjectName("rec")
        self.stackedWidget = QtWidgets.QStackedWidget(self.rec)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1031, 641))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.list_2 = QtWidgets.QListWidget(self.page)
        self.list_2.setGeometry(QtCore.QRect(215, 50, 600, 581))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.list_2.setFont(font)
        self.list_2.setStyleSheet("background-color: rgb(57, 62, 70);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20;")
        self.list_2.setObjectName("list_2")
        self.choose_script = QtWidgets.QLabel(self.page)
        self.choose_script.setGeometry(QtCore.QRect(220, 10, 591, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(18)
        self.choose_script.setFont(font)
        self.choose_script.setStyleSheet("color: #222831;")
        self.choose_script.setObjectName("choose_script")
        self.select = QtWidgets.QPushButton(self.page)
        self.select.setGeometry(QtCore.QRect(820, 90, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.select.setFont(font)
        self.select.setMouseTracking(False)
        self.select.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #FD7013;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #EEEEEE;\n"
"    background-color: #D65F00;\n"
"    border-radius: 10;\n"
"}")
        self.select.setCheckable(False)
        self.select.setObjectName("select")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.listView = QtWidgets.QListView(self.page_2)
        self.listView.setGeometry(QtCore.QRect(20, 50, 801, 261))
        self.listView.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px")
        self.listView.setObjectName("listView")
        self.start = QtWidgets.QPushButton(self.page_2)
        self.start.setGeometry(QtCore.QRect(840, 260, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setMouseTracking(False)
        self.start.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #FD7013;\n"
"    border-radius: 20;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #EEEEEE;\n"
"    background-color: #D65F00;\n"
"    border-radius: 20;\n"
"}")
        self.start.setCheckable(False)
        self.start.setObjectName("start")
        self.choose_script_2 = QtWidgets.QLabel(self.page_2)
        self.choose_script_2.setGeometry(QtCore.QRect(30, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(16)
        self.choose_script_2.setFont(font)
        self.choose_script_2.setStyleSheet("color: #222831;")
        self.choose_script_2.setObjectName("choose_script_2")
        self.change_scene = QtWidgets.QPushButton(self.page_2)
        self.change_scene.setGeometry(QtCore.QRect(840, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.change_scene.setFont(font)
        self.change_scene.setMouseTracking(False)
        self.change_scene.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: rgb(57, 62, 70);\n"
"    border-radius: 15;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #EEEEEE;\n"
"    background-color: #D65F00;\n"
"    border-radius: 15;\n"
"}")
        self.change_scene.setCheckable(False)
        self.change_scene.setObjectName("change_scene")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.tabWidget.addTab(self.rec, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scripts), _translate("MainWindow", "????????????????"))
        self.choose_script.setText(_translate("MainWindow", "???????????????? ????????????????, ???? ???????????????? ?????????? ?????????????????????? ????????????"))
        self.select.setText(_translate("MainWindow", "??????????????????????"))
        self.start.setText(_translate("MainWindow", "???????????? ????????????"))
        self.choose_script_2.setText(_translate("MainWindow", "?????????????????? ????????????????"))
        self.change_scene.setText(_translate("MainWindow", "???????????????? ????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rec), _translate("MainWindow", "???????????? ????????????"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
