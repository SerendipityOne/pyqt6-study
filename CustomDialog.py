from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HELLO!")

        QBtn = (QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        msg = QLabel("Something happened, is that OK?")
        layout.addWidget(msg)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
