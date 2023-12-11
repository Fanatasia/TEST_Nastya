from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app=QApplication([])
win=QWidget()
#створення вікна
win.resize(500,500)
win.setWindowTitle("Тест 1#")
#розмір вікна
title=QLabel("Тестовий додаток")
#назва  вікна
line_h=QHBoxLayout()
line_h.addWidget(title)
#назва вікна2
win.setLayout(line_h)

win.show()

app.exec_()

