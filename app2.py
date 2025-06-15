import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow,QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(400, 300))

    def contextMenuEvent(self, event):
        context = QMenu(self)  # 创建一个上下文菜单
        context.addAction(QAction("test 1", self))  # 创建一个动作
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(event.globalPos())  # 在鼠标位置显示上下文菜单


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
