from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton

def show_win():
    victory_win = QMessageBox()
    victory_win.setText("Ви виграли зустріч з \nтворцями каналу!")
    victory_win.exec()

def show_lose():
    victory_win = QMessageBox()
    victory_win.setText("Пощастить іншим разом!")
    victory_win.exec()

#створення додатка і головного вікна
app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("Конкурс!")
main_win.resize(400, 200)

#створення віджетів головного вікна
question = QLabel("Як звали першого ютуб-блогера, який набрав 100000000 підписників?")
btn_answer1 = QRadioButton("- Рет і Лінк")
btn_answer2 = QRadioButton("- PewDiePie")
btn_answer3 = QRadioButton("- SlivkiShow")
btn_answer4 = QRadioButton("- TheBrianMaps")
btn_answer5 = QRadioButton("- Mister Max")
btn_answer6 = QRadioButton("- EeOneGuy")

#розташування віджетів по лейаутам
layout_main = QVBoxLayout()

layout_h1 = QHBoxLayout()
layout_h2 = QHBoxLayout()
layout_h3 = QHBoxLayout()

layout_h1.addWidget(question, alignment=Qt.AlignCenter)
layout_h2.addWidget(btn_answer1, alignment=Qt.AlignCenter)
layout_h2.addWidget(btn_answer2, alignment=Qt.AlignCenter)
layout_h3.addWidget(btn_answer3, alignment=Qt.AlignCenter)
layout_h3.addWidget(btn_answer4, alignment=Qt.AlignCenter)
layout_h3.addWidget(btn_answer5, alignment=Qt.AlignCenter)
layout_h3.addWidget(btn_answer6, alignment=Qt.AlignCenter)

layout_main.addLayout(layout_h1)
layout_main.addLayout(layout_h2)
layout_main.addLayout(layout_h3)

main_win.setLayout(layout_main)
#обробка натискань на перемикачі
btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_win)
btn_answer3.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)
btn_answer5.clicked.connect(show_lose)
btn_answer6.clicked.connect(show_lose)

#відображення вікна додатка

main_win.show()
app.exec()