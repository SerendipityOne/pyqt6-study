from PyQt6.QtWidgets import QApplication, QWidget
# 仅在访问命令行参数时才需要此设置
import sys

# 每个应用程序都需要一个（且仅需一个） QApplication 实例。
# 将 sys.argv 传入以使您的应用程序能够接受命令行参数。
# 如果您确定不会使用命令行参数，那么使用 QApplication([]) 也是可行的。
app = QApplication(sys.argv)

# 创建一个 Qt 框架组件，它将成为我们的窗口。
window = QWidget()
window.show()  # 重要提示！！！！！ 默认情况下，窗户是隐藏状态的。

# 开始事件循环。
app.exec()

# 应用程序退出时，框架组件也会自动销毁。
