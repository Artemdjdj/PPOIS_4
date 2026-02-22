from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from src.interface.ui.ui_confirmation_to_db_window import Ui_DialogSaveToDb
from src.main.settings import MAIN_WINDOW_ICON


class ConfirmToDbWindow(QDialog):
    confirm_to_db = Signal(bool)

    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogSaveToDb()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(MAIN_WINDOW_ICON))
        self.setWindowTitle("Подтверждение сохранения")
        self.__add_functions()

    def __add_functions(self) -> None:
        self.ui.button_ok.clicked.connect(lambda: self.__confirm_to_save_db(True))
        self.ui.button_cancel.clicked.connect(lambda: self.__confirm_to_save_db(False))

    def __confirm_to_save_db(self, confirmed: bool) -> None:
        self.confirm_to_db.emit(confirmed)
        self.close()
