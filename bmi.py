import sys
from PyQt6.QtWidgets import *


class BMI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        layout = QVBoxLayout()

        self.w = QLineEdit()
        self.h = QLineEdit()
        self.bmi = QLabel("BMI = ")
        self.status = QLabel("Status = ")
        btn = QPushButton("Calculate")
        btn.clicked.connect(self.calc)

        for widget in [QLabel("Weight:"), self.w, QLabel("Height:"), self.h, btn, self.bmi, self.status]:
            layout.addWidget(widget)
        self.setLayout(layout)

    def calc(self):
        b = float(self.w.text()) / float(self.h.text()) ** 2
        self.bmi.setText(f"BMI = {b:.2f}")
        self.status.setText("Status = " + ("Underweight" if b <
                            18.5 else "Normal" if b < 25 else "Overweight" if b < 30 else "Obese"))


app = QApplication(sys.argv)
w = BMI()
w.show()
sys.exit(app.exec())
