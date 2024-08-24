from menu_window import*
from main_window import* 


from random import choice


class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

        self.actual = True
        self.attempts = 0 
        self.correct = 0
    
    def got_right(self):
        
        self.attempts += 1
        self.correct += 1

    def got_wrong(self):
        self.attempts += 1
        

#========================================================================================================
#Питання
#========================================================================================================

q1 = Question('Який грецький бог є головним богом на Олімпі?','Зевс','Посейдон','Арес','Аїд')
q2 = Question('Яка скандинавська богиня є богинею любові і краси?','Фрейя','Хель','Сиф','Ідун')
q3 = Question('Який грецький бог є богом моря?','Посейдон','Гефест','Зевс','Арес')
q4 = Question('Який скандинавський бог відомий своєю силою і молотом?','Тор','Фрейр','Локі','Одін')
q5 = Question('Яка грецька богиня є богинею мудрості і війни?','Афіна','Афродіта','Гера','Артеміда')
q6 = Question('Яка скандинавська істота є могутнім вовком, який буде битись на Рагнароку?','Фенрір','Йормунганд','Сурт','Локі')
q7 = Question('Який скандинавський бог є богом обману і хитрощів?','Локі','Одін','Тор','Фрейр')
q8 = Question('Який грецький герой переміг Мінотавра?','Тесей','Геракл','Персей','Ахіллес')
q9 = Question('Яка скандинавська істота є величезним змієм, що обвиває світ?','Йормунганд','Фенрір','Сурт','Локі')
q10 = Question('Який грецький герой відомий своєю силою і 12 подвигами?','Геракл','Персей','Тесей','Ахіллес')
q11 = Question('Яка скандинавська богиня відповідає за плодовитість і родючість?','Фрейя','Сиф','Ідун','Хель')
q12 = Question('Який грецький бог є покровителем сонця і музики?','Аполлон','Посейдон','Аполон','Зевс')
q13 = Question('Який скандинавський бог є батьком Тора?','Одін','Локі','Фрейр','Тор')
q14 = Question('Яка грецька богиня є богинею полювання і диких тварин?','Артеміда','Афродіта','Афіна','Деметра')
q15 = Question('Який скандинавський бог є богом війни і мудрості?','Одін','Тор','Локі','Фрейр')


#Відповіді:

    #A) Зевс
    #B) Фрейя
    #B) Посейдон
    #B) Тор
    #C) Афіна
    #B) Фенрір
    #C) Локі
    #B) Тесей
    #A) Йормунганд
    #C) Геракл
    #B) Фрейя
    #C) Аполлон
    #A) Одін
    #B) Артеміда
    #A) Одін

#===========================================================================================================
#список з перемакачів кнопок та питань
#===========================================================================================================

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
Questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]

#===========================================================================================================
#Функція що обирає рандомне запитання з списку та показує його на екрані
#===========================================================================================================

def new_question():
    global cur_question
    cur_question = choice(questions)  #вибирає рандомне запитання

    lb_Question.setText(cur_question.question) #встановлює текст (відповіді та запитання) на віджети
    lb_Correct.setText(cur_question.answer)


    shuffle(radio_list)  #перемішує кнопки щоб не 1 була правильна відповідь


    radio_list[0].setText(cur_question.wrong_answer1)  #розмішуємо на них знову запитання
    radio_list[1].setText(cur_question.wrong_answer2)
    radio_list[2].setText(cur_question.wrong_answer3)  #в новому порядку
    radio_list[3].setText(cur_question.answer) 




def check_result



def rest():
    main_win.hide()                    #приховати головний віджет
    n = box_Minutes.value() * 60       #бере значення від користувача і множе на кількість секунд
    sleep(n)                           #спить
    main_win.show()                    #потім знову показує

#=======================================================================================================
#Функції для кнопок панелі
#=======================================================================================================

def show_menu():
    menu_win.show()
    main_win.hide()


def back_menu():
    menu_win.hide()
    main_win.show()

def clear():
    txt_Question.clear()
    txt_Answer.clear()
    txt_Wrong1.clear()
    txt_Wrong2.clear()
    txt_Wrong3.clear()

main_win.show()
app.exec_()


