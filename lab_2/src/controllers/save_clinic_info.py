from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QDialog
from PySide6.QtGui import QIcon
from src.interface.ui.ui_save_window import Ui_Dialog_save
from src.main.settings import MAIN_WINDOW_ICON
from src.db.models.clinic import ClinicInfoBase


class SaveWindow(QDialog):
    cancel = Signal(bool)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_save()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(MAIN_WINDOW_ICON))
        self.setWindowTitle("Сохранение в файл")
        self.__add_functions()

    def __add_functions(self) -> None:
        self.ui.button_ok.clicked.connect(lambda: self.__handle_save(True))
        self.ui.button_cancel.clicked.connect(lambda: self.__handle_save(False))

    def __handle_save(self, confirmed: bool) -> None:
        self.cancel.emit(confirmed)
        self.close()
