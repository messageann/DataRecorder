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
        self.ui.cancel.clicked.connect(self.cancel_script)
        self.ui.save.clicked.connect(self.save)
        self.ui.add_new_action.clicked.connect(self.new_action)
        self.ui.add_act_res.clicked.connect(self.save_action)
        self.ui.action_cancel.clicked.connect(self.cancel_action)
        self.ui.list.itemDoubleClicked.connect(self.selected_item)
        self.ui.delete.clicked.connect(self.delete_script)
        self.ui.actions.itemDoubleClicked.connect(self.activated_action_for_edit)
        self.ui.save_action.clicked.connect(self.edit_action)
        self.ui.record.clicked.connect(self.check_for_code)
        self.ui.delete_action.clicked.connect(self.delete_act)
        self.ui.add_before.clicked.connect(self.new_action_before)
        self.ui.save_before.clicked.connect(self.save_bef)
        self.ui.edit.clicked.connect(self.edit)
        self.ui.save_edit.clicked.connect(self.choose_save)
        self.ui.save_as_new.clicked.connect(self.save)
        self.ui.save_as_old.clicked.connect(self.save_old)
        self.ui.cancel_edit.clicked.connect(self.cancel_script)

    def choose_save(self):
        self.ui.save_as_new.show()
        self.ui.save_as_old.show()
        self.ui.save_edit.clicked.disconnect(self.choose_save)
        self.ui.save_edit.clicked.connect(self.hide_choose)

    def hide_choose(self):
        self.ui.save_as_new.hide()
        self.ui.save_as_old.hide()
        self.ui.save_edit.clicked.disconnect(self.hide_choose)
        self.ui.save_edit.clicked.connect(self.choose_save)

    # Добавление скрипта
    def new_script(self):
        self.clear_frame()
        self.clear_frame2()
        self.ui.frame.show()
        self.ui.edit.hide()
        self.ui.save.show()
        self.ui.name.setReadOnly(False)
        self.ui.delete.hide()
        self.ui.cancel.show()
        self.ui.add_scene.setText('Добавление сценария')

        self.script = Script('')
        try:
            self.ui.actions.itemDoubleClicked.disconnect(self.activated_action_for_show)
            self.ui.actions.itemDoubleClicked.connect(self.activated_action_for_edit)
        except TypeError:
            pass

    # Отмена добавления скрипта
    def cancel_script(self):
        self.clear_frame()
        self.clear_frame2()
        self.ui.frame.hide()
        self.show_scripts()

    # Добавление действия
    def new_action(self):
        self.clear_frame2()
        self.ui.frame_2.show()
        self.ui.action_cancel.show()
        self.ui.add_new_action.hide()
        self.ui.add_act_res.show()
        self.ui.save_before.hide()

    # Добавление действия перед существующим
    def new_action_before(self):
        self.clear_frame2()
        self.ui.frame_2.show()
        self.ui.action_cancel.show()
        self.ui.delete_action.hide()
        self.ui.add_new_action.hide()
        self.ui.add_before.hide()
        self.ui.save_before.show()

    # Сохранение нового действия
    def save_action(self):
        if self.ui.duration.text().isdigit() and self.ui.text.text() != '':
            self.script.add_case(self.ui.code.text(),
                                 self.ui.text.text(),
                                 int(self.ui.duration.text()),
                                 self.ui.record.isChecked())
            self.clear_frame2()
            self.show_actions()
            self.ui.action_cancel.hide()
        else:
            if not self.ui.duration.text().isdigit():
                self.ui.duration.clear()
                self.ui.duration.setPlaceholderText('Введите число!')
            if self.ui.text.text() == '':
                self.ui.text.setPlaceholderText('Введите действие!')

    # Сохранение действия перед существующим
    def save_bef(self):
        curr_key = str(self.ui.actions.currentRow())
        if self.ui.duration.text().isdigit() and self.ui.text.text() != '':
            self.script.add_case_before(self.ui.code.text(),
                                        self.ui.text.text(),
                                        int(self.ui.duration.text()),
                                        self.ui.record.isChecked(),
                                        curr_key)

            self.ui.save_before.hide()
            self.clear_frame2()
            self.show_actions()
            self.ui.action_cancel.hide()
        else:
            if not self.ui.duration.text().isdigit():
                self.ui.duration.clear()
                self.ui.duration.setPlaceholderText('Введите число!')
            if self.ui.text.text() == '':
                self.ui.text.setPlaceholderText('Введите действие!')

    # Проверка необходимости записи
    def check_for_code(self):
        if self.ui.record.isChecked():
            self.ui.code.show()
            self.ui.label_2.show()
        else:
            self.ui.code.hide()
            self.ui.code.clear()
            self.ui.label_2.hide()

    # Отменя добавления действия
    def cancel_action(self):
        self.clear_frame2()
        self.ui.frame_2.hide()
        self.ui.add_new_action.show()
        self.ui.add_act_res.hide()
        self.ui.action_cancel.hide()

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
        try:
            self.ui.save_edit.clicked.disconnect(self.hide_choose)
            self.ui.save_edit.clicked.connect(self.choose_save)
        except TypeError:
            pass

    # Пересохранение сценария
    def save_old(self):
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
        self.ui.save_edit.clicked.disconnect(self.hide_choose)
        self.ui.save_edit.clicked.connect(self.choose_save)

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

    # Удаление существующего действия
    def delete_act(self):
        key = str(self.ui.actions.currentRow())
        self.script.delete_action(key)
        self.show_actions()
        self.ui.delete_action.hide()
        self.clear_frame2()
        self.ui.action_cancel.hide()

    # Показать действия в сценарии
    def show_actions(self):
        self.ui.actions.clear()
        acts = self.script.get_acts()
        for act in acts:
            self.ui.actions.addItem(act)

    # Выбор действия
    def activated_action_for_show(self, item_selected):
        self.ui.frame_2.show()
        key = str(self.ui.actions.currentRow())
        self.ui.code.setText(self.script.actions[key]['label'])
        self.ui.code.setReadOnly(True)
        self.ui.text.setText(self.script.actions[key]['text'])
        self.ui.text.setReadOnly(True)
        self.ui.duration.setText(str(self.script.actions[key]['duration']))
        self.ui.duration.setReadOnly(True)
        self.ui.record.setChecked(self.script.actions[key]['record'])
        self.check_for_code()
        self.ui.record.setEnabled(False)
        self.ui.add_new_action.hide()
        self.ui.act_info.show()

    def activated_action_for_edit(self, item_selected):
        self.ui.frame_2.show()
        self.ui.save_action.show()
        self.ui.action_cancel.show()
        self.ui.delete_action.show()
        self.ui.add_before.show()
        key = str(self.ui.actions.currentRow())
        self.ui.code.setText(self.script.actions[key]['label'])
        self.ui.text.setText(self.script.actions[key]['text'])
        self.ui.duration.setText(str(self.script.actions[key]['duration']))
        self.ui.record.setChecked(self.script.actions[key]['record'])
        self.check_for_code()
        self.ui.add_new_action.hide()

    # Редактирование существующего действия
    def edit_action(self):
        key = str(self.ui.actions.currentRow())
        if self.ui.duration.text().isdigit() and self.ui.text.text() != '':
            self.script.actions[key]['label'] = self.ui.code.text()
            self.script.actions[key]['text'] = self.ui.text.text()
            self.script.actions[key]['duration'] = int(self.ui.duration.text())
            self.script.actions[key]['record'] = self.ui.record.isChecked()
            self.ui.frame_2.hide()
            self.ui.save_action.hide()
            self.ui.add_act_res.hide()
            self.ui.add_new_action.show()
            self.show_actions()
            self.ui.action_cancel.hide()
            self.ui.delete_action.hide()
            self.ui.add_before.hide()
        else:
            if not self.ui.duration.text().isdigit():
                self.ui.duration.clear()
                self.ui.duration.setPlaceholderText('Введите число!')
            if self.ui.text.text() == '':
                self.ui.text.setPlaceholderText('Введите действие!')

    # Просмотр выбранного сценария
    def selected_item(self, item):
        self.clear_frame()
        self.clear_frame2()
        self.ui.add_scene.setText('Просмотр сценария')
        self.ui.frame.show()
        self.ui.name.setText(item.text())
        self.ui.name.setReadOnly(True)
        self.ui.cancel.hide()
        self.ui.save.hide()
        self.ui.edit.show()
        self.ui.add_new_action.hide()
        self.ui.delete.show()
        try:
            self.ui.actions.itemDoubleClicked.disconnect(self.activated_action_for_edit)
            self.ui.actions.itemDoubleClicked.connect(self.activated_action_for_show)
        except TypeError:
            pass

        sc = os.listdir(os.getcwd() + '\\scripts')
        for file in sc:
            if file == item.text() + '.json':
                self.script = Script(item.text())
                with open('scripts\\' + file, 'r') as js:
                    self.script.actions = json.load(js)
        acts = self.script.get_acts()
        for act in acts:
            self.ui.actions.addItem(act)

    # Изменение сценария
    def edit(self):
        self.ui.add_scene.setText('Изменение сценария')
        self.ui.add_new_action.show()
        self.ui.name.setReadOnly(False)
        self.ui.edit.hide()
        self.ui.delete.hide()
        self.ui.cancel_edit.show()
        self.ui.save_edit.show()
        self.show_actions()
        self.clear_frame2()
        self.ui.frame_2.hide()
        self.ui.act_info.hide()
        try:
            self.ui.actions.itemDoubleClicked.disconnect(self.activated_action_for_show)
            self.ui.actions.itemDoubleClicked.connect(self.activated_action_for_edit)
        except TypeError:
            pass

    # Отобразить все скрипты
    def show_scripts(self):
        self.ui.list.clear()
        sc = os.listdir(os.getcwd() + '\\scripts')
        for file in sc:
            self.ui.list.addItem(os.path.splitext(file)[0])

    # Очистить правую часть
    def clear_frame(self):
        self.ui.name.clear()
        self.ui.actions.clear()
        self.ui.code.clear()
        self.ui.text.clear()
        self.ui.duration.clear()
        self.ui.record.setChecked(False)
        self.ui.frame_2.hide()
        self.ui.add_new_action.show()
        self.ui.save_action.hide()
        self.ui.action_cancel.hide()
        self.ui.delete_action.hide()
        self.ui.add_act_res.hide()
        self.ui.save_edit.hide()
        self.ui.save_as_new.hide()
        self.ui.save_as_old.hide()
        self.ui.cancel_edit.hide()

    # Очистить добавление действия
    def clear_frame2(self):
        self.ui.code.clear()
        self.ui.text.clear()
        self.ui.text.setPlaceholderText('')
        self.ui.duration.clear()
        self.ui.duration.setPlaceholderText('миллисек.')
        self.ui.record.show()
        self.ui.frame_2.hide()
        self.ui.add_act_res.hide()
        self.ui.save_action.hide()
        self.ui.add_new_action.show()
        self.ui.delete_action.hide()
        self.ui.code.setReadOnly(False)
        self.ui.text.setReadOnly(False)
        self.ui.duration.setReadOnly(False)
        self.ui.record.setEnabled(True)
        self.ui.act_info.hide()
        self.ui.add_before.hide()
