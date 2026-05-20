from PyQt6.QtWidgets import *
from gui import BMI


class Welcome(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome")
        self.resize(300, 150)

        layout = QVBoxLayout()

        title = QLabel("Welcome to BMI Calculator")
        title.setStyleSheet("font-size: 18px;")

        button = QPushButton("Start")
        button.clicked.connect(self.open_bmi)

        layout.addWidget(title)
        layout.addWidget(button)

        self.setLayout(layout)

    def open_bmi(self):
        self.bmi = BMI()
        self.bmi.show()
        self.close()
