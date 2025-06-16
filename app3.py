import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,  # 复选框
            QComboBox,  # 下拉列表框
            QDateEdit,  # 用于编辑日期和日期时间
            QDateTimeEdit,  # 用于编辑日期和日期时间
            QDial,  # 可旋转表盘
            QDoubleSpinBox,  # 浮点数微调器
            QFontComboBox,  # 字体列表
            QLCDNumber,  # 相当丑陋的 LCD 显示屏
            QLabel,  # 只是一个标签，而不是交互式的
            QLineEdit,  # 输入一行文本
            QProgressBar,  # 进度条
            QPushButton,  # 一个按钮
            QRadioButton,  # 只有一个活动项的切换集
            QSlider,  # 滑块
            QSpinBox,  # 整数微调器
            QTimeEdit,  # 对于编辑时间
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
