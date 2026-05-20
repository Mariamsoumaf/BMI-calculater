from PyQt6.QtWidgets import *
from logic import calculate_bmi


class BMI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI Calculator")
        self.resize(300, 200)

        self.setStyleSheet("""
            QWidget {
                font-size: 14px;
            }

            QPushButton {
                background-color: lightblue;
                padding: 5px;
            }
        """)

        layout = QVBoxLayout()

        self.w = QLineEdit()
        self.h = QLineEdit()

        self.bmi = QLabel("BMI = ")
        self.status = QLabel("Status = ")

        btn = QPushButton("Calculate")
        btn.clicked.connect(self.calc)

        widgets = [
            QLabel("Weight:"),
            self.w,
            QLabel("Height:"),
            self.h,
            btn,
            self.bmi,
            self.status,
        ]

        for widget in widgets:
            layout.addWidget(widget)

        self.setLayout(layout)

    def calc(self):
        if self.w.text() == "" or self.h.text() == "":
            self.status.setText("Please enter values")
            return

        weight = float(self.w.text())
        height = float(self.h.text())

        bmi, status = calculate_bmi(weight, height)

        self.bmi.setText(f"BMI = {bmi:.2f}")
        self.status.setText(f"Status = {status}")
