#підключення модулів
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import*
from random import randint

app = QApplication([]) #обєкт програмування

#основне вікно
main_wind = QWidget()
main_wind.resize(400,400)
main_wind.move(100,100)
main_wind.setWindowTitle("Лотерея")


#створюємо віджети (кнопки та надписи)
num1 = QLabel("?")
num2 = QLabel("?")
text = QLabel("Натисни, щоб взяти участь")
button = QPushButton("Випробувати удачу")

# розміщення віджетів
line = QVBoxLayout()
line.addWidget(text,alignment= Qt.AlignCenter)
line.addWidget(num1,alignment= Qt.AlignCenter)
line.addWidget(num2,alignment= Qt.AlignCenter)
line.addWidget(button,alignment= Qt.AlignCenter)

main_wind.setLayout(line)

def rand():
    n1 = randint(0,9)
    n2 = randint(0,9)
    num1.setText(str(n1))
    num2.setText(str(n2))
    if n1 == n2:
        text.setText("Ви виграли! Зіграйте знову")
    else:
        text.setText("Ви програли! Зіграйте знову")

button.clicked.connect(rand)

main_wind.show() #показати вікно
app.exec_() #щоб автоматично не завершувалася
