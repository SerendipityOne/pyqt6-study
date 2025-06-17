import sys
from random import randint

from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QApplication


class AnotherWindow(QWidget):
    """
    这个“窗口”是一个 QWidget。如果它没有父窗口，就会像我们期望的那样以自由浮动窗口的形式出现。
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        """
        %d 格式化（%-formatting）是 Python 早期版本的字符串格式化方式，语法较为传统。
        {} 格式化（f-string）是 Python 3.6+ 引入的新特性，更直观、简洁，且支持直接在字符串中嵌入表达式。
        """
        # self.label = QLabel("Another Window %d" % randint(0, 100))
        self.label = QLabel(f"Another Window {randint(0, 100)}")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        self.w = AnotherWindow()
        self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
