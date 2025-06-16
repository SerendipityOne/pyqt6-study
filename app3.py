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

        widget = QSlider(Qt.Orientation.Vertical) # 创建垂直方向的滑块（默认）
        # widget = QSlider(Qt.Orientation.Horizontal) # 创建水平方向的滑块

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        widget.setSingleStep(3)

        widget.valueChanged.connect(self.value_changed)  # 当滑块的值改变时触发
        widget.sliderMoved.connect(self.slider_position)  # 当滑块移动时触发
        widget.sliderPressed.connect(self.slider_pressed)  # 当滑块按下时触发
        widget.sliderReleased.connect(self.slider_released)  # 当滑块释放时触发

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("Position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
