import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setFixedSize(QSize(400, 300))
        self.setWindowTitle("My App")

        # button = QPushButton("Click me")
        # button.setCheckable(True)
        # button.clicked.connect(self.the_button_was_clicked)
        # button.clicked.connect(self.the_button_was_toggled)

        self.button = QPushButton("Click me")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

    def the_button_was_clicked(self):
        print("Clicked")

    # QPushButton 的 toggled 信号会在按钮的状态改变时被触发，并且会自动传递一个布尔值 checked 给连接的槽（slot）或函数
    def the_button_was_toggled(self, checked):
        # print("Checked?", checked)
        self.button_is_checked = checked
        print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
