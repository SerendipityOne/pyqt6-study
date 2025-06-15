import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 200))

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)  # 将输入框内容绑定到标签上

        layout = QVBoxLayout()  # 垂直布局
        layout.addWidget(self.input)  # 添加输入框到布局
        layout.addWidget(self.label)

        container = QWidget()  # 创建容器
        container.setLayout(layout)  # 设置布局

        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
