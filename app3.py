import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        widget = QLabel("Hello, PyQt!")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setPixmap(QPixmap("otje.jpg"))  # 设置 QLabel 的背景图片。
        widget.setScaledContents(True)  # 让 QLabel 的内容自适应大小。
        # 将 QLabel 中的文本设置为水平和垂直居中对齐。
        # widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
