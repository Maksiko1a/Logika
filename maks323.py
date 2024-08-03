from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*





def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Правильно!')
    victory_win.exec_()

def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('Не правильно!')
    victory_win.exec_()




app = QApplication([])
main_win = QWidget()


main_win.setWindowTitle("Конкурс від Crazy People")
main_win.resize(400,200)


quastion = QLabel("Як звали першого ютуб-блогера, який набрав 100 000 000 підписників")
btn_answer1 = QRadioButton('PewDiePie')
btn_answer2 = QRadioButton('MrBeast')
btn_answer3 = QRadioButton('SlivkiShow')
btn_answer4 = QRadioButton('TheBrianMaps')


layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layout_main = QVBoxLayout()

layoutH1.addWidget(quastion, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)


layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)



btn_answer1.clicked.connect(show_win)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)


main_win.setLayout(layout_main)
main_win.show()
app.exec_()

