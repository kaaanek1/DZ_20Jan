  import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer, QPoint

class CatchGame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Catch the Red Button")
        self.setGeometry(100, 100, 800, 600)

        self.green_button = QPushButton()
        self.green_button.setStyleSheet("background-color: green;")
        self.green_button.setFixedSize(50, 50)

        self.red_button = QPushButton()
        self.red_button.setStyleSheet("background-color: red;")
        self.red_button.setFixedSize(50, 50)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.green_button)
        self.layout.addWidget(self.red_button)
        self.setLayout(self.layout)

        # Устанавливаем начальные позиции кнопок
        self.red_button.move(random.randint(0, 750), random.randint(0, 550))
        self.green_button.move(0, 0)

        self.timer = QTimer()
        self.timer.timeout.connect(self.move_green_button)
        self.timer.start(50)  # обновление каждые 50 мс

        self.speed = 8 # Увеличиваем скорость до 5 пикселей

    def move_green_button(self):
        green_pos = self.green_button.pos()
        red_pos = self.red_button.pos()

        # Двигаем зеленую кнопку к красной
        if green_pos.x() < red_pos.x():
            green_pos.setX(green_pos.x() + self.speed)
        elif green_pos.x() > red_pos.x():
            green_pos.setX(green_pos.x() - self.speed)

        if green_pos.y() < red_pos.y():
            green_pos.setY(green_pos.y() + self.speed)
        elif green_pos.y() > red_pos.y():
            green_pos.setY(green_pos.y() - self.speed)

        self.green_button.move(green_pos)

        # Проверяем, догнала ли зеленая кнопка красную
        if green_pos.x() < red_pos.x() + 50 and green_pos.x() + 50 > red_pos.x() and \
           green_pos.y() < red_pos.y() + 50 and green_pos.y() + 50 > red_pos.y():
            self.red_button.move(random.randint(0, 750), random.randint(0, 550))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = CatchGame()
    game.show()
    sys.exit(app.exec_())
