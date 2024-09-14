from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.generate)
    
    def generate(self):        #генерація паролю
        signs=""
        if self.ui.cb_alphabet.isChecked():
            signs +="qwertyuiopasdfghjklzxcvbnm"
        if self.ui.cb_numbers.isChecked():
            signs +="0123456789"

        result = ""
        number = random.randint(5,10)    #може випасти пароль від 5 до 10 чисел
        for _ in range(number):
            result+=random.choice(signs)

        self.ui.result.setText(result)




app = QApplication([])
ex = Widget()
ex.show()
app.exec_()