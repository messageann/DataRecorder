from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from script import Script
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scripts beta')
        self.ui.add.clicked.connect(self.new_script)
        self.show_scripts()

    def show_scripts(self):
        self.ui.list.clear()
        sc = os.listdir(os.getcwd() + '\scripts')
        for file in sc:
            self.ui.list.addItem(os.path.splitext(file)[0])

    def show_actions(self):
        self.ui.actions.setText(self.script.make_str())

    def new_script(self):
        self.ui.frame.setVisible(True)
        self.ui.add_act.clicked.connect(self.new_action)
        self.ui.save.clicked.connect(self.save)
        self.show_scripts()
        self.script = Script('')

    def new_action(self):
        self.show_scripts()
        self.ui.frame_2.setVisible(True)
        self.ui.add_act_res.setVisible(True)
        self.ui.add_act_res.clicked.connect(self.act_info)
        self.ui.add_act_2.clicked.connect(self.add_rest)

    def act_info(self):
        if self.ui.duration.text() != '':
            self.script.add_case(self.ui.code.text(),
                                 self.ui.text.text(),
                                 int(self.ui.duration.text()),
                                 self.ui.record_2.isChecked())
        if self.ui.duration_rest.text() != '':
            self.script.add_rest(int(self.ui.duration_rest.text()))

        self.ui.code.clear()
        self.ui.text.clear()
        self.ui.duration.clear()
        self.ui.frame_2.setVisible(False)
        self.ui.add_act_res.setVisible(False)
        self.show_actions()

    def add_rest(self):
        self.ui.duration_rest.setVisible(True)
        self.ui.add_act_3.setVisible(True)
        self.ui.add_act_3.clicked.connect(self.reset_rest)

    def reset_rest(self):
        self.ui.duration_rest.clear()
        self.ui.duration_rest.setVisible(False)
        self.ui.add_act_3.setVisible(False)

    def save(self):
        if self.ui.name.text() != '':
            self.script._name = self.ui.name.text()
            self.script.save_script()
        self.ui.frame.setVisible(False)
        self.show_scripts()
        self.ui.actions.clear()
        self.ui.name.clear()
