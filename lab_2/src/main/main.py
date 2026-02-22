import sys
from PySide6.QtWidgets import QApplication

from src.controllers.main_clinic_info import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
