from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 550)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("background-color:#f4f5f9;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1000, 531))
        self.tabWidget.setStyleSheet("background-color: #f4f5f9;")
        self.tabWidget.setObjectName("tabWidget")

        self.scripts = QtWidgets.QWidget()
        self.scripts.setObjectName("scripts")

        self.all_scenes = QtWidgets.QLabel(self.scripts)
        self.all_scenes.setGeometry(QtCore.QRect(20, 20, 280, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(15)
        self.all_scenes.setFont(font)
        self.all_scenes.setStyleSheet("color: #222831;")
        self.all_scenes.setObjectName("all_scenes")

        self.list = QtWidgets.QListWidget(self.scripts)
        self.list.setGeometry(QtCore.QRect(20, 70, 460, 380))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.list.setFont(font)
        self.list.setStyleSheet("background-color: rgb(57, 62, 70);\n"
                                "color: rgb(255, 255, 255);\n"
                                "border-radius: 20;\n"
                                "padding-left: 15px;\n"
                                "padding-top: 7px;\n"
                                "padding-right: 15px;"
                                )
        self.list.setObjectName("list")

        self.add = QtWidgets.QPushButton(self.scripts)
        self.add.setGeometry(QtCore.QRect(300, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setMouseTracking(False)
        self.add.setStyleSheet("QPushButton {\n"
                               "    color: white;\n"
                               "    background-color: #FD7013;\n"
                               "    border-radius: 15;\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "    color: #EEEEEE;\n"
                               "    background-color: #D65F00;\n"
                               "    border-radius: 15;\n"
                               "}")
        self.add.setCheckable(False)
        self.add.setObjectName("add")

        self.frame = QtWidgets.QFrame(self.scripts)
        self.frame.setVisible(False)
        self.frame.setGeometry(QtCore.QRect(520, 20, 460, 431))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setPlaceholderText("Название скрипта")
        self.name.setGeometry(QtCore.QRect(20, 50, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.name.setFont(font)
        self.name.setStyleSheet("border-radius: 20;\n"
                                "background-color: rgb(255, 255, 255);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")

        self.add_scene = QtWidgets.QLabel(self.frame)
        self.add_scene.setGeometry(QtCore.QRect(20, 0, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(15)
        self.add_scene.setFont(font)
        self.add_scene.setStyleSheet("color: #222831;")
        self.add_scene.setObjectName("add_scene")

        self.add_act = QtWidgets.QPushButton(self.frame)
        self.add_act.setGeometry(QtCore.QRect(20, 223, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.add_act.setFont(font)
        self.add_act.setMouseTracking(False)
        self.add_act.setStyleSheet("QPushButton {\n"
                                   "    color: white;\n"
                                   "    background-color: #393E46;\n"
                                   "    border-radius: 15;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "    color: #EEEEEE;\n"
                                   "    background-color: #222831;\n"
                                   "    border-radius: 15;\n"
                                   "}")
        self.add_act.setCheckable(False)
        self.add_act.setObjectName("add_act")

        self.check = QtWidgets.QComboBox(self.frame)
        self.check.setGeometry(QtCore.QRect(140, 223, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.check.setFont(font)
        self.check.setMouseTracking(False)
        self.check.setStyleSheet("border-radius: 15;\n"
                                 "background-color: white;")
        self.check.setObjectName("check")

        self.add_act_res = QtWidgets.QPushButton(self.frame)
        self.add_act_res.setGeometry(QtCore.QRect(20, 223, 111, 31))
        self.add_act_res.setVisible(False)
        self.add_act_res.setText('Добавить')
        self.add_act_res.setFont(font)
        self.add_act_res.setMouseTracking(False)
        self.add_act_res.setStyleSheet("QPushButton {\n"
                                       "    color: white;\n"
                                       "    background-color: #FD7013;\n"
                                       "    border-radius: 15;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    color: #EEEEEE;\n"
                                       "    background-color: #D65F00;\n"
                                       "    border-radius: 15;\n"
                                       "}")
        self.add_act_res.setCheckable(False)
        self.add_act_res.setObjectName("add_act")

        self.save_act = QtWidgets.QPushButton(self.frame)
        self.save_act.setGeometry(QtCore.QRect(20, 223, 111, 31))
        self.save_act.setVisible(False)
        self.save_act.setText('Сохранить')
        self.save_act.setFont(font)
        self.save_act.setMouseTracking(False)
        self.save_act.setStyleSheet("QPushButton {\n"
                                    "    color: white;\n"
                                    "    background-color: #FD7013;\n"
                                    "    border-radius: 15;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    color: #EEEEEE;\n"
                                    "    background-color: #D65F00;\n"
                                    "    border-radius: 15;\n"
                                    "}")
        self.save_act.setCheckable(False)
        self.save_act.setObjectName("save_act")

        self.actions = QtWidgets.QTextBrowser(self.frame)
        self.actions.setPlaceholderText('Тут будет содержимое сценария')
        self.actions.setGeometry(QtCore.QRect(20, 100, 420, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.actions.setFont(font)
        self.actions.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 20;\n"
                                   "padding-left: 10px;\n"
                                   "padding-top: 3px;\n"
                                   "padding-right: 10px;")
        self.actions.setObjectName("actions")

        self.save = QtWidgets.QPushButton(self.frame)
        self.save.setGeometry(QtCore.QRect(340, 5, 101, 30))
        self.save.setText('Сохранить')
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setMouseTracking(False)
        self.save.setStyleSheet("QPushButton {\n"
                                "    color: white;\n"
                                "    background-color: #FD7013;\n"
                                "    border-radius: 15;\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "    color: #EEEEEE;\n"
                                "    background-color: #D65F00;\n"
                                "    border-radius: 15;\n"
                                "}")
        self.save.setCheckable(False)
        self.save.setObjectName("save")

        self.edit = QtWidgets.QPushButton(self.frame)
        self.edit.setGeometry(QtCore.QRect(340, 5, 101, 30))
        self.edit.setText('Изменить')
        self.edit.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edit.setFont(font)
        self.edit.setMouseTracking(False)
        self.edit.setStyleSheet("QPushButton {\n"
                                "    color: white;\n"
                                "    background-color: #FD7013;\n"
                                "    border-radius: 15;\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "    color: #EEEEEE;\n"
                                "    background-color: #D65F00;\n"
                                "    border-radius: 15;\n"
                                "}")
        self.edit.setCheckable(False)
        self.edit.setObjectName("edit")

        self.save_edit = QtWidgets.QPushButton(self.frame)
        self.save_edit.setGeometry(QtCore.QRect(340, 5, 101, 30))
        self.save_edit.setText('Сохранить')
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_edit.setFont(font)
        self.save_edit.setMouseTracking(False)
        self.save_edit.setStyleSheet("QPushButton {\n"
                                     "    color: white;\n"
                                     "    background-color: #FD7013;\n"
                                     "    border-radius: 15;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    color: #EEEEEE;\n"
                                     "    background-color: #D65F00;\n"
                                     "    border-radius: 15;\n"
                                     "}")
        self.save_edit.setCheckable(False)
        self.save_edit.setObjectName("save_edit")
        self.save_edit.setVisible(False)

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setVisible(False)
        self.frame_2.setGeometry(QtCore.QRect(19, 259, 421, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.code = QtWidgets.QLineEdit(self.frame_2)
        self.code.setPlaceholderText('Метка класса')
        self.code.setGeometry(QtCore.QRect(0, 10, 191, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.code.setFont(font)
        self.code.setStyleSheet("border-radius: 15;\n"
                                "background-color: rgb(255, 255, 255);")
        self.code.setAlignment(QtCore.Qt.AlignCenter)
        self.code.setObjectName("code")

        self.text = QtWidgets.QLineEdit(self.frame_2)
        self.text.setPlaceholderText('Текст команды')
        self.text.setGeometry(QtCore.QRect(0, 53, 420, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.text.setFont(font)
        self.text.setStyleSheet("border-radius: 15;\n"
                                "background-color: rgb(255, 255, 255);")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")

        self.record_2 = QtWidgets.QCheckBox(self.frame_2)
        self.record_2.setGeometry(QtCore.QRect(220, 100, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(8)
        self.record_2.setFont(font)
        self.record_2.setObjectName("record_2")

        self.duration = QtWidgets.QLineEdit(self.frame_2)
        self.duration.setPlaceholderText('Длительность (сек.)')
        self.duration.setGeometry(QtCore.QRect(0, 95, 191, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.duration.setFont(font)
        self.duration.setStyleSheet("border-radius: 15;\n"
                                    "background-color: rgb(255, 255, 255);")
        self.duration.setAlignment(QtCore.Qt.AlignCenter)
        self.duration.setObjectName("duration")

        self.add_act_2 = QtWidgets.QPushButton(self.frame_2)
        self.add_act_2.setGeometry(QtCore.QRect(0, 140, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.add_act_2.setFont(font)
        self.add_act_2.setMouseTracking(False)
        self.add_act_2.setStyleSheet("QPushButton {\n"
                                     "    color: white;\n"
                                     "    background-color: #393E46;\n"
                                     "    border-radius: 15;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    color: #EEEEEE;\n"
                                     "    background-color: #222831;\n"
                                     "    border-radius: 15;\n"
                                     "}")
        self.add_act_2.setCheckable(False)
        self.add_act_2.setObjectName("add_act_2")

        self.add_act_3 = QtWidgets.QPushButton(self.frame_2)
        self.add_act_3.setGeometry(QtCore.QRect(0, 140, 221, 30))
        self.add_act_3.setText('Отмена')
        self.add_act_3.setFont(font)
        self.add_act_3.setMouseTracking(False)
        self.add_act_3.setStyleSheet("QPushButton {\n"
                                     "    color: white;\n"
                                     "    background-color: #FD7013;\n"
                                     "    border-radius: 15;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    color: #EEEEEE;\n"
                                     "    background-color: #D65F00;\n"
                                     "    border-radius: 15;\n"
                                     "}")
        self.add_act_3.setCheckable(False)
        self.add_act_3.setObjectName("add_act_2")
        self.add_act_3.setVisible(False)

        self.duration_rest = QtWidgets.QLineEdit(self.frame_2)
        self.duration_rest.setPlaceholderText('Длительность (сек.)')
        self.duration_rest.setVisible(False)
        self.duration_rest.setEnabled(True)
        self.duration_rest.setGeometry(QtCore.QRect(230, 140, 191, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.duration_rest.setFont(font)
        self.duration_rest.setStyleSheet("border-radius: 15;\n"
                                         "background-color: rgb(255, 255, 255);")
        self.duration_rest.setAlignment(QtCore.Qt.AlignCenter)
        self.duration_rest.setObjectName("duration_rest")

        self.tabWidget.addTab(self.scripts, "")
        self.record = QtWidgets.QWidget()
        self.record.setObjectName("record")
        self.tabWidget.addTab(self.record, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 21))
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.all_scenes.setText(_translate("MainWindow", "Существующие сценарии"))
        self.add.setText(_translate("MainWindow", "Добавить сценарий"))
        self.add_scene.setText(_translate("MainWindow", "Добавление сценария"))
        self.add_act.setText(_translate("MainWindow", "Новое действие"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.record_2.setText(_translate("MainWindow", "Записывать данные на шаге"))
        self.add_act_2.setText(_translate("MainWindow", "Добавить фазу отдыха"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scripts), _translate("MainWindow", "Сценарии"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.record), _translate("MainWindow", "Запись данных"))
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
