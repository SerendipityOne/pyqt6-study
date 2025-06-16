from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)  # 开启背景填充功能

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))  # 设置背景颜色
        self.setPalette(palette)
