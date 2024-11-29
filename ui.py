from PyQt6.QtWidgets import QPushButton, QGraphicsView, QVBoxLayout, QWidget


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.layout = QVBoxLayout(self.centralwidget)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.layout.addWidget(self.graphicsView)

        self.pushButton = QPushButton('Сгенерировать круги', self.centralwidget)
        self.layout.addWidget(self.pushButton)
