import sys
import random

from ui import Ui_MainWindow
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsEllipseItem


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Colorful Circles')
        self.setFixedSize(400, 300)

        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)

        self.pushButton.clicked.connect(self.add_circles)

    def add_circle(self) -> None:
        diameter = random.randint(20, 100)
        x = random.randint(0, 380 - diameter)
        y = random.randint(0, 230 - diameter)

        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        ellipse = QGraphicsEllipseItem(x, y, diameter, diameter)
        ellipse.setBrush(color)
        self.scene.addItem(ellipse)

    def add_circles(self) -> None:
        self.scene.clear()

        for _ in range(10):
            self.add_circle()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
