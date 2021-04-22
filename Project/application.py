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
        self.ui.cancel.clicked.connect(self.cancel)
        self.ui.delete_act.clicked.connect(self.delete_act)
        self.ui.add_before.clicked.connect(self.before)
        self.ui.add_bf.clicked.connect(self.save_before)
        self.ui.cancel_script.clicked.connect(self.cancel_scr)
        self.ui.del_script.clicked.connect(self.delete_script)

    # Добавление скрипта
    def new_script(self):
        self.clear_frame()
        self.ui.frame.show()
        self.ui.edit.hide()
        self.ui.save.show()
        self.ui.name.setReadOnly(False)
        self.ui.del_script.hide()
        self.ui.cancel_script.show()
        self.ui.add_scene.setText('Добавление сценария')

        self.script = Script('')

    # Отмена добавления скрипта
    def cancel_scr(self):
        self.clear_frame()
        self.clear_frame2()
        self.ui.frame.hide()
        self.show_scripts()

    # Добавление действия
    def new_action(self):
        self.clear_frame2()
        self.ui.frame_2.show()
        self.ui.cancel.show()
        self.ui.add_act.hide()
        self.ui.add_act_res.show()
        self.ui.add_act_2.show()

    # Добавление действия перед существующим
    def before(self):
        self.clear_frame2()
        self.ui.frame_2.show()
        self.ui.cancel.show()
        self.ui.delete_act.hide()
        self.ui.add_act.hide()
        self.ui.add_bf.show()
        self.ui.add_before.hide()

    # Сохранение действия перед существующим
    def save_before(self):
        curr_key = self.ui.check.currentText()
        if self.ui.duration.text() == '':
            self.ui.duration.setText('0')
        self.script.add_case_before(self.ui.code.text(),
                                    self.ui.text.text(),
                                    int(self.ui.duration.text()),
                                    self.ui.record_2.isChecked(),
                                    curr_key)

        self.ui.add_bf.hide()
        self.clear_frame2()
        self.show_actions()
        self.list_of_act()
        self.ui.cancel.hide()

    # Отменя добавления действия
    def cancel(self):
        self.clear_frame2()
        self.ui.frame_2.hide()
        self.ui.cancel.show()
        self.ui.add_act.show()
        self.ui.add_act_res.hide()
        self.ui.cancel.hide()
        self.ui.add_bf.hide()
        self.list_of_act()

    # Сохранение нового сценария
    def save(self):
        if self.ui.name.text() == '':
            self.script.name = 'Unnamed script'
        else:
            self.script.name = self.ui.name.text()
        self.script.save_script()
        self.clear_frame()
        self.clear_frame2()
        self.ui.frame.hide()
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
        self.ui.frame.hide()
        self.show_scripts()

    # Удаление существующего сценария
    def delete_script(self):
        sc = os.listdir(os.getcwd() + '\\scripts')
        for file in sc:
            if file == self.script.name + '.json':
                os.remove('scripts\\' + file)

        self.clear_frame()
        self.clear_frame2()
        self.ui.frame.hide()
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
        self.ui.cancel.hide()

    # Удаление существующего действия
    def delete_act(self):
        key = self.ui.check.currentText()
        self.script.delete_action(key)
        self.show_actions()
        self.ui.delete_act.hide()
        self.clear_frame2()
        self.list_of_act()

    # Показать действия в сценарии
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
            self.ui.frame_2.show()
            self.ui.code.setText(self.script.actions[item_selected]['label'])
            self.ui.text.setText(self.script.actions[item_selected]['text'])
            self.ui.duration.setText(str(self.script.actions[item_selected]['duration']))
            self.ui.record_2.setChecked(self.script.actions[item_selected]['record'])
            self.ui.add_act_2.hide()
            self.ui.save_act.show()
            self.ui.delete_act.show()
            self.ui.add_before.show()
        else:
            self.clear_frame2()
            self.ui.add_bf.hide()
            self.ui.cancel.hide()

    # Редактирование существующего действия
    def edit_action(self):
        key = self.ui.check.currentText()
        if key != '':
            self.script.actions[key]['label'] = self.ui.code.text()
            self.script.actions[key]['text'] = self.ui.text.text()
            self.script.actions[key]['duration'] = int(self.ui.duration.text())
            self.script.actions[key]['record'] = self.ui.record_2.isChecked()
            self.ui.frame_2.hide()
            self.ui.save_act.hide()
            self.ui.add_act_res.hide()
            self.ui.add_act.show()
            self.show_actions()
            self.list_of_act()
        else:
            self.clear_frame2()

    # Просмотр выбранного сценария
    def selected_item(self, item):
        self.clear_frame()
        self.clear_frame2()
        self.ui.add_scene.setText('Просмотр сценария')
        self.ui.actions.setGeometry(QtCore.QRect(20, 100, 420, 331))
        self.ui.frame.show()
        self.ui.save.hide()
        self.ui.save_edit.hide()
        self.ui.edit.show()
        self.ui.check.hide()
        self.ui.add_act.hide()
        self.ui.name.setText(item.text())
        self.ui.name.setReadOnly(True)
        self.ui.del_script.show()
        self.ui.cancel_script.hide()
        sc = os.listdir(os.getcwd() + '\\scripts')
        for file in sc:
            if file == item.text() + '.json':
                self.script = Script(item.text())
                with open('scripts\\' + file, 'r') as js:
                    self.script.actions = json.load(js)
        self.ui.actions.setText(self.script.make_str())

    # Изменение сценария
    def edit_item(self):
        self.ui.add_scene.setText('Изменение сценария')
        self.ui.actions.setGeometry(QtCore.QRect(20, 100, 420, 111))
        self.ui.add_act.show()
        self.ui.name.setReadOnly(False)
        self.ui.check.show()
        self.ui.edit.hide()
        self.ui.save_edit.show()
        self.show_actions()
        self.list_of_act()

    # Отобразить все скрипты
    def show_scripts(self):
        self.ui.list.clear()
        sc = os.listdir(os.getcwd() + '\\scripts')
        for file in sc:
            self.ui.list.addItem(os.path.splitext(file)[0])

    # Добавление фазы отдыха
    def add_rest(self):
        self.ui.duration_rest.show()
        self.ui.add_act_2.hide()
        self.ui.add_act_3.show()

    # Отмена добавления фазы отдыха
    def reset_rest(self):
        self.ui.duration_rest.clear()
        self.ui.duration_rest.hide()
        self.ui.add_act_3.hide()
        self.ui.add_act_2.show()
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
        self.ui.frame_2.hide()
        self.ui.add_act.show()
        self.ui.save_act.hide()
        self.ui.check.show()
        self.ui.actions.setGeometry(QtCore.QRect(20, 100, 420, 111))
        self.ui.cancel.hide()
        self.ui.delete_act.hide()
        self.ui.add_act_res.hide()
        self.ui.add_bf.hide()

    # Очистить добавление действия
    def clear_frame2(self):
        self.ui.code.clear()
        self.ui.text.clear()
        self.ui.duration.clear()
        self.ui.record_2.show()
        self.ui.frame_2.hide()
        self.ui.add_act_res.hide()
        self.ui.save_act.hide()
        self.ui.add_before.hide()
        self.ui.add_act.show()