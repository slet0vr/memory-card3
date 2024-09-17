from PyQt5.QtWidgets import QApplication, QWidget
from random import shuffle
app = QApplication([])
from layout_quizz import *
from question import *

i = 0

window = QWidget()
window.resize(600, 500)
window.setWindowTitle('Memory Card')
window.setLayout(main_line_quizz)
window.show()
shuffle(questions)
questions[i].show_question(question_label, rb1, rb2, rb3, rb4)

def click_ok():
    global i
    if btn_ok.text() == "Відповісти":
        radio_group_box.hide()
        ansradio_group_box.show()
        btn_ok.setText("Наступне питання")
    else:
        radio_group_box.show()
        ansradio_group_box.hide()
        btn_ok.setText("Відповісти")
        i += 1
        questions[i].show_question(question_label, rb1, rb2, rb3, rb4)
btn_ok.clicked.connect(click_ok)
app.exec()