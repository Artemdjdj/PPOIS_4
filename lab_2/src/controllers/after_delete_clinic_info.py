from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from src.interface.ui.ui_after_delete_window import Ui_AfterDeleteWindow
from src.main.settings import MAIN_WINDOW_ICON


class AfterDeleteWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AfterDeleteWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(MAIN_WINDOW_ICON))
        self.setWindowTitle("Результат удаления")
        self.__add_functions()

    def __add_functions(self) -> None:
        self.ui.button_ok.clicked.connect(lambda: self.close())
