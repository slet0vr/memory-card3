from PyQt5.QtWidgets import QPushButton, QRadioButton, QLabel, QVBoxLayout, QSpinBox, QGroupBox, QButtonGroup, QHBoxLayout
from PyQt5.QtCore import Qt
btn_menu = QPushButton("меню")
btn_rest = QPushButton("Відпочити")
spin = QSpinBox()
spin.setValue(30)

    
layout = QVBoxLayout()

radio_group_box = QGroupBox("Варіанти відповіді:")
btn_ok = QPushButton("Відповісти")

rb1 = QRadioButton("caterpillar")
rb2 = QRadioButton("apple")
rb3 = QRadioButton("aplication")
rb4 = QRadioButton("building")


main_box_line = QHBoxLayout()
box_line1 = QVBoxLayout()
box_line2 = QVBoxLayout()
box_line1.addWidget(rb1)
box_line1.addWidget(rb2)
box_line2.addWidget(rb3)
box_line2.addWidget(rb4)
main_box_line.addLayout(box_line1)
main_box_line.addLayout(box_line2)
radio_group_box.setLayout(main_box_line)

ansradio_group_box = QGroupBox("результати теста")
main_box2_line = QVBoxLayout()
result_lb = QLabel("правильно")
right_ans_lb = QLabel("apple")
main_box2_line.addWidget(result_lb, alignment=Qt.AlignTop)
main_box2_line.addWidget(right_ans_lb)
ansradio_group_box.setLayout(main_box2_line)
ansradio_group_box.hide()

radio_button_group = QButtonGroup()
radio_button_group.addButton(rb1)
radio_button_group.addButton(rb2)
radio_button_group.addButton(rb3)
radio_button_group.addButton(rb4)



question_label = QLabel("Яблуко")
layout.addWidget(question_label)





main_line_quizz = QVBoxLayout()
line1_quizz = QHBoxLayout()
line1_quizz.addWidget(btn_menu)
line1_quizz.addStretch(1)
line1_quizz.addWidget(btn_rest)
line1_quizz.addWidget(spin)
line1_quizz.addWidget(QLabel("хвилин"))

main_line_quizz.addLayout(line1_quizz, stretch=1)
main_line_quizz.addWidget(question_label, alignment = Qt.AlignCenter)
main_line_quizz.addWidget(radio_group_box, stretch=5)
main_line_quizz.addWidget(ansradio_group_box, stretch=5)
main_line_quizz.addWidget(btn_ok, stretch=1)