import sys
from random import randint

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QApplication


class AnotherWindow(QWidget):
    """
    这个“窗口”是一个 QWidget。如果它没有父窗口，就会像我们期望的那样以自由浮动窗口的形式出现。
    """

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(300, 150))
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
        self.setFixedSize(QSize(400, 300))

        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        l = QVBoxLayout()
        button1 = QPushButton("Push for Window 1")
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        l.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
