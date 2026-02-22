from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from src.interface.ui.ui_confirmation_delete_window import Ui_ConfirmDialog
from src.main.settings import MAIN_WINDOW_ICON


class ConfirmWindow(QDialog):
    delete = Signal(bool)

    def __init__(self):
        super().__init__()
        self.ui = Ui_ConfirmDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(MAIN_WINDOW_ICON))
        self.setWindowTitle("Подтверждения удаления")
        self.__add_functions()

    def __add_functions(self) -> None:
        self.ui.button_ok.clicked.connect(lambda: self.__handle_delete(True))
        self.ui.button_cancel.clicked.connect(lambda: self.__handle_delete(False))

    def __handle_delete(self, confirmed: bool) -> None:
        self.delete.emit(confirmed)
        self.close()
