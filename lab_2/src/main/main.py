import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIcon
from src.interface.ui.ui_main_window import Ui_MainWindow
from src.main.settings import MAIN_WINDOW_ICON

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(MAIN_WINDOW_ICON))

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
