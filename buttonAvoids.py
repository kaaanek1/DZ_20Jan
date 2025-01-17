import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class EscapingButton(QPushButton):
    def __init__(self, name):
        super().__init__(name)
        self.setFixedSize(100, 50)

    def enterEvent(self, event):
        # Перемещаем кнопку в случайное место в пределах окна
        self.moveRandomly()
        super().enterEvent(event)


    def moveRandomly(self):
        parent = self.parent()
        if parent:
            x = random.randint(0, parent.width() - self.width())
            y = random.randint(0, parent.height() - self.height())
            self.move(x, y)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("blablabla?")
        self.setFixedSize(800, 600)

        self.button = EscapingButton("Net")

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
