from PyQt5 import QtGui

# FONTS

# Labels
font_for_labels = QtGui.QFont()
font_for_labels.setFamily("Bahnschrift SemiCondensed")
font_for_labels.setPointSize(15)

# Text in fields
default_font = QtGui.QFont()
default_font.setFamily("Bahnschrift Light")
default_font.setPointSize(10)

# List
font_list = QtGui.QFont()
font_list.setFamily("Bahnschrift Light")
font_list.setPointSize(12)

# Check record
font_check = QtGui.QFont()
font_check.setFamily("Bahnschrift Light")
font_check.setPointSize(8)

# Big btn
font_big_btn = QtGui.QFont()
font_big_btn.setFamily("Bahnschrift SemiBold")
font_big_btn.setPointSize(10)
font_big_btn.setBold(True)
font_big_btn.setWeight(75)

# Little btn
font_ltl_btn = QtGui.QFont()
font_ltl_btn.setFamily("Bahnschrift SemiBold")
font_ltl_btn.setPointSize(8)
font_ltl_btn.setBold(True)
font_ltl_btn.setWeight(75)

# STYLE SHEETS
only_background = "background-color: #f4f5f9;"

color_labels = "color: #222831;"

for_list = ("background-color: rgb(57, 62, 70);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 20;\n"
            "padding-left: 15px;\n"
            "padding-top: 7px;\n"
            "padding-right: 15px;")

for_orange_btn = ("QPushButton {\n"
                  "    color: white;\n"
                  "    background-color: #FD7013;\n"
                  "    border-radius: 15;\n"
                  "}\n"
                  "\n"
                  "QPushButton:hover {\n"
                  "    color: white;\n"
                  "    background-color: #FF822E;\n"
                  "    border-radius: 15;\n"
                  "}"
                  "\n"
                  "QPushButton:pressed {\n"
                  "    color: #EDEDD5;\n"
                  "    background-color: #F06A11;\n"
                  "    border-radius: 15;\n"
                  "}")

for_line_edit = ("border-radius: 15;\n"
                 "background-color: rgb(255, 255, 255);")

for_btn = ("QPushButton {\n"
           "    color: white;\n"
           "    background-color: #393E46;\n"
           "    border-radius: 15;\n"
           "}\n"
           "\n"
           "QPushButton:hover {\n"
           "    color: white;\n"
           "    background-color: #46545C;\n"
           "    border-radius: 15;\n"
           "}\n"
           "\n"
           "QPushButton:pressed {\n"
           "    color: #E5EDE1;\n"
           "    background-color: #292D33;\n"
           "    border-radius: 15;\n"
           "}")

for_combobox = ("border-radius: 15;\n"
                "background-color: white;")

for_actions = ("background-color: rgb(255, 255, 255);\n"
               "border-radius: 20;\n"
               "padding-left: 10px;\n"
               "padding-top: 3px;\n"
               "padding-right: 10px;")

