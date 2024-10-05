from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
import json


# Функція для запису у файл
def writeToFile():
    with open("notes.json","w") as file:
        json.dump(notes,file,sort_keys=True)





#============================================================================================================
# Вікно програми
#============================================================================================================

app = QApplication([])
window = QWidget()
window.setWindowTitle("Smart Notes")
window.resize(800,600)
window.move(0,0)
window.setStyleSheet("background-color: rgb(255, 255, 153); font-size: 15px")


#============================================================================================================
# Елементи інтерфейсу
#============================================================================================================

text_editor = QTextEdit()
text_editor.setPlaceholderText("Введіть текст замітки...")

list_widget_1 = QListWidget()  #список заміток
list_widget_2 = QListWidget()  #список тегів


text_searcher = QLineEdit()             #пошук по тексту
text_searcher.setPlaceholderText("Введіть текст .....")

tag_searcher = QLineEdit()              #пошук по тегу
tag_searcher.setPlaceholderText("Введіть тег .....")

#============================================================================================================
# Створюємо кнопки
#============================================================================================================

make_note = QPushButton()
make_note.setText("Створити замітку")

delete_note = QPushButton()
delete_note.setText("Видалити замітку")

save_note = QPushButton()
save_note.setText("Зберегти замітку")

search_for_text = QPushButton()
search_for_text.setText("Шукати за текстом")

search_for_tag = QPushButton()
search_for_tag.setText("Шукати за тегом")

add_to_note = QPushButton()
add_to_note.setText("Додати тег до замітки")

unpin_to_note = QPushButton()
unpin_to_note.setText("Відкріпити тег від замітки")

convert_to_txt = QPushButton()
convert_to_txt.setText("Конвертувати до txt формату")

action_theme_btn = QPushButton()
action_theme_btn.setText("Змінити тему")

#============================================================================================================
# Макет
#============================================================================================================

row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1 = QVBoxLayout()
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список заміток:"))
col2.addWidget(list_widget_1)
col2.addLayout(row1)
col2.addWidget(save_note)

col2.addWidget(QLabel("Список тегів"))
col2.addWidget(list_widget_2)
col2.addWidget(QLabel("Пошук даних"))
col2.addWidget(tag_searcher)
col2.addWidget(text_searcher)
col2.addLayout(row2)

# Нижні 3 кнопки
col2.addWidget(search_for_tag)
col2.addWidget(search_for_text)
col2.addWidget(convert_to_txt)
col2.addWidget(action_theme_btn)

# Злиття
layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)


# Макет на екран
window.setLayout(layout_note)


text_editor.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 15px")
list_widget_1.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 15px")
list_widget_2.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 15px")
text_searcher.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 15px")
tag_searcher.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 15px")
make_note.setStyleSheet("background-color: rgb(255, 191, 0); font-size: 15px")
delete_note.setStyleSheet("background-color: rgb(255, 191, 0); font-size: 15px")
save_note.setStyleSheet("background-color: rgb(255, 191, 0); font-size: 15px")
add_to_note.setStyleSheet("background-color: rgb(255, 191, 0); font-size: 15px")
unpin_to_note.setStyleSheet("background-color: rgb(255, 191, 0); font-size: 15px")
search_for_tag.setStyleSheet("background-color: rgb(255, 191, 0); font-size: 15px")
search_for_text.setStyleSheet("background-color: rgb(255, 191, 0); font-size: 15px")
convert_to_txt.setStyleSheet("background-color: rgb(255, 191, 0); font-size: 15px")
action_theme_btn.setStyleSheet("background-color: rgb(255, 191, 0); font-size: 15px")

#==========================================================================================================
# Функціонал програми
#==========================================================================================================

#  отримуємо текст із замітки з виділеною назвою та відображаємо його в полі редагування
def show_notes():
    global key                                                # назва замітки - ключ
    key = list_widget_1.selectedItems()[0].text()     # дізнаємось на яку записку клікнули
    list_widget_1.clear()                             # очищаємо поле із тегами
    text_editor.setText(notes[key]["text"])           # відобразили текст замітки
    list_widget_1.addItems(notes[key]["tag"])         # відобразили теги замітки

def add_notes():
    note_name,ok = QInputDialog.getText(window,"Додати замітку","Назва замітки:")
    if note_name and ok:
        list_widget_1.addItems(note_name)
        notes[note_name] = {"text":"","tag":""}
    writeToFile()

def delete_notes():
    if list_widget_1.currentItem():
        if key in notes:
            notes.pop(key)

        text_editor.clear()
        list_widget_1.clear()
        list_widget_2.clear()

        list_widget_1.addItem(notes)
        writeToFile()

def save_notes():
    if list_widget_1.currentItem():
        key = list_widget_1.currentItem().text()
        notes[key]["text"] = text_editor.toPlainText()
        writeToFile()
    
#Підключаємо функція до віджету
list_widget_1.clicked.connect(show_notes)
make_note.clicked.connect(add_notes)
delete_note.clicked.connect(delete_notes)
save_note.clicked.connect(save_notes)



#Зчитуємо файл
with open("notes.json","r") as file:
    notes = json.load(file)
list_widget_1.addItems(notes)




#Закриття програми та показ
window.show()
app.exec_()