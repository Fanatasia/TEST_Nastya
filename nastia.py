from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app=QApplication([])
win=QWidget()

win.resize(500,500)
win.setWindowTitle("Тест 1#")

title=QLabel("Тестовий додаток")

line_h=QHBoxLayout()
line_h.addWidget(title)

win.setLayout(line_h)

win.show()

app.exec_()

