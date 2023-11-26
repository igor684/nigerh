from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()

window.resize(500, 500)

lbl = QLabel("Вікторина")
numberlbl = QLabel("Номер переможця")
startBtn = QPushButton("Дізнатися переможця")
main_line = QVBoxLayout()
main_line.addWidget(lbl)
main_line.addWidget(numberlbl)
main_line.addWidget(startBtn)
window.setLayout(main_line)
window.show()
app.exec()