''' Головне вікно для картки запитання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *



app = QApplication([])

#----------------------------------------------------------------------------------------------------------
#Створення вікна
#----------------------------------------------------------------------------------------------------------
menu_win = QWidget()
menu_win.resize(400, 300)             #розмір вікна
menu_win.setWindowTitle("Меню")    #назва вікна

txt_Question = QLineEdit("")
txt_Answer = QLineEdit("")
txt_Wrong1 = QLineEdit("")
txt_Wrong2 = QLineEdit("")
txt_Whong3 = QLineEdit("")


layout_form = QFormLayout()
layout_form.addRow("Питання:",txt_Question)
layout_form.addRow("Правильна відповідь:",txt_Answer)
layout_form.addRow("Неправильний варіант №1:",txt_Wrong1)
layout_form.addRow("Неправильний варіант №2:",txt_Wrong2)
layout_form.addRow("Неправильний варіант №3:",txt_Whong3)

btn_add_q = QPushButton("Додати запитання")
btn_back = QPushButton("Назад")
btn_clear = QPushButton("Очистити")


lbl_statistics = QLabel('')


lbl_statistics = QLabel('Статистика:\nПравильних відповідей: 0\nЗагальну кількість спроб: 0')

hbtn = QHBoxLayout()
hbtn.addWidget(btn_back)
hbtn.addWidget(btn_add_q)
hbtn.addWidget(btn_clear)


vline = QVBoxLayout()
vline.addLayout(layout_form)
vline.addLayout(hbtn)
vline.addWidget(lbl_statistics)

menu_win.setLayout(vline)

menu_win.show()
app.exec_()
