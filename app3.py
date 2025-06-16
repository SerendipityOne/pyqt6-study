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

        widget = QDial()  # 创建一个旋钮控件
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)  # 绑定旋钮值改变信号
        widget.sliderMoved.connect(self.slider_position)  # 绑定滑块位置改变信号
        widget.sliderPressed.connect(self.slider_pressed)  # 绑定滑块按下信号
        widget.sliderReleased.connect(self.slider_released)  # 绑定滑块释放信号

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
