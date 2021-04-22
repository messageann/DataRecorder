from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from script import Script
import os
import json


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scripts beta')
        self.show_scripts()

        self.ui.add.clicked.connect(self.new_script)
        self.ui.list.itemDoubleClicked.connect(self.selected_item)
        self.ui.add_act.clicked.connect(self.new_action)
        self.ui.save.clicked.connect(self.save)
        self.ui.add_act_res.clicked.connect(self.save_action)
        self.ui.add_act_2.clicked.connect(self.add_rest)
        self.ui.check.activated[str].connect(self.activated_act)
        self.ui.save_act.clicked.connect(self.edit_action)
        self.ui.edit.clicked.connect(self.edit_item)
        self.ui.add_act_3.clicked.connect(self.reset_rest)
        self.ui.save_edit.clicked.connect(self.save_edit)

    # Добавление скрипта
    def new_script(self):
        self.clear_frame()
        self.ui.frame.setVisible(True)
        self.ui.edit.setVisible(False)
        self.ui.save.setVisible(True)
        self.ui.name.setReadOnly(False)
        self.ui.add_scene.setText('Добавление сценария')

        self.script = Script('')

    # Добавление действия
    def new_action(self):
        self.clear_frame2()
        self.ui.frame_2.setVisible(True)
        self.ui.add_act.setVisible(False)
        self.ui.add_act_res.setVisible(True)
        self.ui.add_act_2.setVisible(True)

    # Сохранение сценария
    def save(self):
        if self.ui.name.text() == '':
            self.script.name = 'Unnamed script'
        else:
            self.script.name = self.ui.name.text()
        self.script.save_script()
        self.clear_frame()
        self.clear_frame2()
        self.ui.frame.setVisible(False)
        self.show_scripts()

    # Сохранение переименнованного сценария
    def save_edit(self):
        old = self.script.name
        sc = os.listdir(os.getcwd() + '\\scripts')
        for file in sc:
            if file == old + '.json':
                os.remove('scripts\\' + file)
        if self.ui.name.text() == '':
            self.script.name = 'Unnamed script'
        else:
            self.script.name = self.ui.name.text()
        self.script.save_script()
        self.clear_frame()
        self.clear_frame2()
        self.ui.frame.setVisible(False)
        self.show_scripts()

    # Сохранение нового действия
    def save_action(self):
        if self.ui.duration.text() == '':
            self.ui.duration.setText('0')
        self.script.add_case(self.ui.code.text(),
                             self.ui.text.text(),
                             int(self.ui.duration.text()),
                             self.ui.record_2.isChecked())
        if self.ui.duration_rest.text() != '':
            self.script.add_rest(int(self.ui.duration_rest.text()))

        self.clear_frame2()
        self.reset_rest()
        self.show_actions()
        self.list_of_act()

    # Действия в сценарии
    def show_actions(self):
        self.ui.actions.setText(self.script.make_str())

    # Заполнение чекбокса
    def list_of_act(self):
        self.ui.check.clear()
        acts = ['']
        for a in self.script.actions.keys():
            acts.append(a)
        self.ui.check.addItems(acts)

    # Выбор действия в чекбоксе
    def activated_act(self, item_selected):
        if item_selected != '':
            self.ui.frame_2.setVisible(True)
            self.ui.code.setText(self.script.actions[item_selected]['label'])
            self.ui.text.setText(self.script.actions[item_selected]['text'])
            self.ui.duration.setText(str(self.script.actions[item_selected]['duration']))
            self.ui.record_2.setChecked(self.script.actions[item_selected]['record'])
            self.ui.add_act_2.setVisible(False)
            self.ui.save_act.setVisible(True)
        else:
            self.clear_frame2()

    # Отредактированное действие
    def edit_action(self):
        key = self.ui.check.currentText()
        if key != '':
            self.script.actions[key]['label'] = self.ui.code.text()
            self.script.actions[key]['text'] = self.ui.text.text()
            self.script.actions[key]['duration'] = int(self.ui.duration.text())
            self.script.actions[key]['record'] = self.ui.record_2.isChecked()
            self.ui.frame_2.setVisible(False)
            self.ui.save_act.setVisible(False)
            self.ui.add_act_res.setVisible(False)
            self.ui.add_act.setVisible(True)
            self.show_actions()
            self.list_of_act()
        else:
            self.clear_frame2()

    # Выбранный сценарий
    def selected_item(self, item):
        self.clear_frame()
        self.clear_frame2()
        self.ui.add_scene.setText('Просмотр сценария')
        self.ui.actions.setGeometry(QtCore.QRect(20, 100, 420, 331))
        self.ui.frame.setVisible(True)
        self.ui.save.setVisible(False)
        self.ui.save_edit.setVisible(False)
        self.ui.edit.setVisible(True)
        self.ui.check.setVisible(False)
        self.ui.add_act.setVisible(False)
        self.ui.name.setText(item.text())
        self.ui.name.setReadOnly(True)
        sc = os.listdir(os.getcwd() + '\\scripts')
        for file in sc:
            if file == item.text() + '.json':
                self.script = Script(item.text())
                with open('scripts\\' + file, 'r') as js:
                    self.script.actions = json.load(js)
        self.ui.actions.setText(self.script.make_str())

    def edit_item(self):
        self.ui.add_scene.setText('Изменение сценария')
        self.ui.actions.setGeometry(QtCore.QRect(20, 100, 420, 111))
        self.ui.add_act.setVisible(True)
        self.ui.name.setReadOnly(False)
        self.ui.check.setVisible(True)
        self.ui.edit.setVisible(False)
        self.ui.save_edit.setVisible(True)
        self.show_actions()
        self.list_of_act()

    # Все скрипты
    def show_scripts(self):
        self.ui.list.clear()
        sc = os.listdir(os.getcwd() + '\\scripts')
        for file in sc:
            self.ui.list.addItem(os.path.splitext(file)[0])

    # Добавление фазы отдыха
    def add_rest(self):
        self.ui.duration_rest.setVisible(True)
        self.ui.add_act_2.setVisible(False)
        self.ui.add_act_3.setVisible(True)

    # Отмена добавления фазы отдыха
    def reset_rest(self):
        self.ui.duration_rest.clear()
        self.ui.duration_rest.setVisible(False)
        self.ui.add_act_3.setVisible(False)
        self.ui.add_act_2.setVisible(True)
        return

    # Очистить правую часть
    def clear_frame(self):
        self.ui.name.clear()
        self.ui.actions.clear()
        self.ui.check.clear()
        self.ui.code.clear()
        self.ui.text.clear()
        self.ui.duration.clear()
        self.ui.record_2.setChecked(False)
        self.ui.frame_2.setVisible(False)
        self.ui.add_act.setVisible(True)
        self.ui.save_act.setVisible(False)
        self.ui.check.setVisible(True)
        self.ui.actions.setGeometry(QtCore.QRect(20, 100, 420, 111))

    # Очистить добавление действия
    def clear_frame2(self):
        self.ui.code.clear()
        self.ui.text.clear()
        self.ui.duration.clear()
        self.ui.record_2.setChecked(False)
        self.ui.frame_2.setVisible(False)
        self.ui.add_act_res.setVisible(False)
        self.ui.add_act.setVisible(True)
