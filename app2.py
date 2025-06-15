import sys
from random import choice

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow

window_titles = [
    'My App',
    'Still My App',
    'What on earth',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 200))

        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.the_button_was_clicked)  # 连接按钮点击信号
        self.windowTitleChanged.connect(self.the_window_title_changed)  # 连接窗口标题改变信号

        self.setCentralWidget(self.button)

    # 按钮被点击时调用的槽函数
    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    # 当窗口标题改变时调用的槽函数
    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == "Something went wrong":
            self.button.setText("You can't click me anymore")
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
