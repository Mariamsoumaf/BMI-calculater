import sys
from PyQt6.QtWidgets import QApplication
from welcome import Welcome

app = QApplication(sys.argv)

window = Welcome()
window.show()

sys.exit(app.exec())
