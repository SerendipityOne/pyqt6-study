from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文本居中

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))  # 设置图标大小
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("bug.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.toolbar_button_clicked)
        button_action.setCheckable(True)
        button_action.setShortcut(QKeySequence("Ctrl+p")) # 设置快捷键
        toolbar.addAction(button_action)

        toolbar.addSeparator()  # 添加分割线

        button_action2 = QAction(QIcon("bug.png"), "&Your button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.toolbar_button_clicked)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello!"))
        toolbar.addWidget(QCheckBox("Check me!"))

        self.setStatusBar(QStatusBar(self))  # 添加状态栏

        menu = self.menuBar() # 添加菜单栏

        file_menu = menu.addMenu("&File") # 添加文件菜单
        file_menu.addAction(button_action)
        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submenu") # 添加子菜单
        file_submenu.addAction(button_action2)

    def toolbar_button_clicked(self, s):
        print("click", s)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
