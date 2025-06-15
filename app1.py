from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt6.QtCore import QSize, Qt
import sys


# 继承 QMainWindow 类以自定义您的应用程序的主窗口
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Click me")

        # self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(500, 500))

        # 设置窗口的中心部件。
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
