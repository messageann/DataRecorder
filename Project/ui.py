from PyQt5 import QtCore, QtGui, QtWidgets
import styles


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 562)
        MainWindow.setStyleSheet(styles.only_background)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1000, 562))
        self.tabWidget.setStyleSheet(styles.only_background)
        self.tabWidget.setObjectName("tabWidget")

        self.scripts = QtWidgets.QWidget()
        self.scripts.setObjectName("scripts")

        self.all_scenes = QtWidgets.QLabel(self.scripts)
        self.all_scenes.setGeometry(QtCore.QRect(20, 20, 280, 41))
        self.all_scenes.setFont(styles.font_for_labels)
        self.all_scenes.setStyleSheet(styles.color_labels)
        self.all_scenes.setObjectName("all_scenes")

        self.list = QtWidgets.QListWidget(self.scripts)
        self.list.setGeometry(QtCore.QRect(20, 70, 460, 380))
        self.list.setFont(styles.font_list)
        self.list.setStyleSheet(styles.for_list)
        self.list.setObjectName("list")

        self.add = QtWidgets.QPushButton(self.scripts)
        self.add.setGeometry(QtCore.QRect(300, 30, 181, 31))
        self.add.setFont(styles.font_big_btn)
        self.add.setMouseTracking(False)
        self.add.setStyleSheet(styles.for_orange_btn)
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
        self.name.setFont(styles.default_font)
        self.name.setStyleSheet(styles.for_line_edit)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")

        self.add_scene = QtWidgets.QLabel(self.frame)
        self.add_scene.setGeometry(QtCore.QRect(20, 0, 321, 41))
        self.add_scene.setFont(styles.font_for_labels)
        self.add_scene.setStyleSheet(styles.color_labels)
        self.add_scene.setObjectName("add_scene")

        self.add_act = QtWidgets.QPushButton(self.frame)
        self.add_act.setGeometry(QtCore.QRect(20, 223, 111, 31))
        self.add_act.setFont(styles.font_ltl_btn)
        self.add_act.setMouseTracking(False)
        self.add_act.setStyleSheet(styles.for_btn)
        self.add_act.setCheckable(False)
        self.add_act.setObjectName("add_act")

        self.check = QtWidgets.QComboBox(self.frame)
        self.check.setGeometry(QtCore.QRect(140, 223, 111, 31))
        self.check.setFont(styles.default_font)
        self.check.setMouseTracking(False)
        self.check.setStyleSheet(styles.for_combobox)
        self.check.setObjectName("check")

        self.add_act_res = QtWidgets.QPushButton(self.frame)
        self.add_act_res.setGeometry(QtCore.QRect(20, 223, 111, 31))
        self.add_act_res.setVisible(False)
        self.add_act_res.setText('Добавить')
        self.add_act_res.setFont(styles.font_ltl_btn)
        self.add_act_res.setMouseTracking(False)
        self.add_act_res.setStyleSheet(styles.for_orange_btn)
        self.add_act_res.setCheckable(False)
        self.add_act_res.setObjectName("add_act")

        self.add_bf = QtWidgets.QPushButton(self.frame)
        self.add_bf.setGeometry(QtCore.QRect(20, 223, 111, 31))
        self.add_bf.setVisible(False)
        self.add_bf.setText('Добавить перед')
        self.add_bf.setFont(styles.font_ltl_btn)
        self.add_bf.setMouseTracking(False)
        self.add_bf.setStyleSheet(styles.for_orange_btn)
        self.add_bf.setCheckable(False)
        self.add_bf.setObjectName("add_act")

        self.save_act = QtWidgets.QPushButton(self.frame)
        self.save_act.setGeometry(QtCore.QRect(20, 223, 111, 31))
        self.save_act.setVisible(False)
        self.save_act.setText('Сохранить')
        self.save_act.setFont(styles.font_ltl_btn)
        self.save_act.setMouseTracking(False)
        self.save_act.setStyleSheet(styles.for_orange_btn)
        self.save_act.setCheckable(False)
        self.save_act.setObjectName("save_act")

        self.actions = QtWidgets.QTextBrowser(self.frame)
        self.actions.setPlaceholderText('Тут будет содержимое сценария')
        self.actions.setGeometry(QtCore.QRect(20, 100, 420, 111))
        self.actions.setFont(styles.default_font)
        self.actions.setStyleSheet(styles.for_actions)
        self.actions.setObjectName("actions")

        self.save = QtWidgets.QPushButton(self.frame)
        self.save.setGeometry(QtCore.QRect(340, 5, 101, 30))
        self.save.setText('Сохранить')
        self.save.setFont(styles.font_big_btn)
        self.save.setMouseTracking(False)
        self.save.setStyleSheet(styles.for_orange_btn)
        self.save.setCheckable(False)
        self.save.setObjectName("save")

        self.edit = QtWidgets.QPushButton(self.frame)
        self.edit.setGeometry(QtCore.QRect(340, 5, 101, 30))
        self.edit.setText('Изменить')
        self.edit.setVisible(False)
        self.edit.setFont(styles.font_big_btn)
        self.edit.setMouseTracking(False)
        self.edit.setStyleSheet(styles.for_orange_btn)
        self.edit.setCheckable(False)
        self.edit.setObjectName("edit")

        self.save_edit = QtWidgets.QPushButton(self.frame)
        self.save_edit.setGeometry(QtCore.QRect(340, 5, 101, 30))
        self.save_edit.setText('Сохранить')
        self.save_edit.setFont(styles.font_big_btn)
        self.save_edit.setMouseTracking(False)
        self.save_edit.setStyleSheet(styles.for_orange_btn)
        self.save_edit.setCheckable(False)
        self.save_edit.setObjectName("save_edit")
        self.save_edit.setVisible(False)

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setVisible(False)
        self.frame_2.setGeometry(QtCore.QRect(19, 259, 421, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.cancel = QtWidgets.QPushButton(self.frame)
        self.cancel.setGeometry(QtCore.QRect(330, 223, 111, 31))
        self.cancel.setFont(styles.font_ltl_btn)
        self.cancel.setText('Отменить')
        self.cancel.setMouseTracking(False)
        self.cancel.setStyleSheet(styles.for_btn)
        self.cancel.setCheckable(False)
        self.cancel.setObjectName("сancel")
        self.cancel.setVisible(False)

        self.delete_act = QtWidgets.QPushButton(self.frame)
        self.delete_act.setGeometry(QtCore.QRect(330, 223, 111, 31))
        self.delete_act.setFont(styles.font_ltl_btn)
        self.delete_act.setText('Удалить')
        self.delete_act.setMouseTracking(False)
        self.delete_act.setStyleSheet(styles.for_btn)
        self.delete_act.setCheckable(False)
        self.delete_act.setObjectName("delete_act")
        self.delete_act.setVisible(False)

        self.code = QtWidgets.QLineEdit(self.frame_2)
        self.code.setPlaceholderText('Метка класса')
        self.code.setGeometry(QtCore.QRect(0, 10, 191, 30))
        self.code.setFont(styles.default_font)
        self.code.setStyleSheet(styles.for_line_edit)
        self.code.setAlignment(QtCore.Qt.AlignCenter)
        self.code.setObjectName("code")

        self.text = QtWidgets.QLineEdit(self.frame_2)
        self.text.setPlaceholderText('Текст команды')
        self.text.setGeometry(QtCore.QRect(0, 53, 420, 30))
        self.text.setFont(styles.default_font)
        self.text.setStyleSheet(styles.for_line_edit)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")

        self.record_2 = QtWidgets.QCheckBox(self.frame_2)
        self.record_2.setGeometry(QtCore.QRect(220, 100, 201, 20))
        self.record_2.setFont(styles.font_check)
        self.record_2.setObjectName("record_2")

        self.duration = QtWidgets.QLineEdit(self.frame_2)
        self.duration.setPlaceholderText('Длительность (сек.)')
        self.duration.setGeometry(QtCore.QRect(0, 95, 191, 30))
        self.duration.setFont(styles.default_font)
        self.duration.setStyleSheet(styles.for_line_edit)
        self.duration.setAlignment(QtCore.Qt.AlignCenter)
        self.duration.setObjectName("duration")

        self.add_act_2 = QtWidgets.QPushButton(self.frame_2)
        self.add_act_2.setGeometry(QtCore.QRect(0, 140, 221, 30))
        self.add_act_2.setFont(styles.font_ltl_btn)
        self.add_act_2.setMouseTracking(False)
        self.add_act_2.setStyleSheet(styles.for_btn)
        self.add_act_2.setCheckable(False)
        self.add_act_2.setObjectName("add_act_2")

        self.add_act_3 = QtWidgets.QPushButton(self.frame_2)
        self.add_act_3.setGeometry(QtCore.QRect(0, 140, 221, 30))
        self.add_act_3.setText('Отмена')
        self.add_act_3.setFont(styles.font_ltl_btn)
        self.add_act_3.setMouseTracking(False)
        self.add_act_3.setStyleSheet(styles.for_orange_btn)
        self.add_act_3.setCheckable(False)
        self.add_act_3.setObjectName("add_act_3")
        self.add_act_3.setVisible(False)

        self.add_before = QtWidgets.QPushButton(self.frame_2)
        self.add_before.setGeometry(QtCore.QRect(0, 140, 221, 30))
        self.add_before.setFont(styles.font_ltl_btn)
        self.add_before.setMouseTracking(False)
        self.add_before.setText('Добавить действие перед')
        self.add_before.setVisible(False)
        self.add_before.setStyleSheet(styles.for_btn)
        self.add_before.setCheckable(False)
        self.add_before.setObjectName("add_before")

        self.duration_rest = QtWidgets.QLineEdit(self.frame_2)
        self.duration_rest.setPlaceholderText('Длительность (сек.)')
        self.duration_rest.setVisible(False)
        self.duration_rest.setEnabled(True)
        self.duration_rest.setGeometry(QtCore.QRect(230, 140, 191, 30))
        self.duration_rest.setFont(styles.default_font)
        self.duration_rest.setStyleSheet(styles.for_line_edit)
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
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
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
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
