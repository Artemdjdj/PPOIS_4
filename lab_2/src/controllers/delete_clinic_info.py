import sys
from datetime import date
from typing import List
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QDialog
from PySide6.QtGui import QIcon

from src.main.data_saver import DataSaver
from src.exceptions.exceptions import BirthdayError, DateOfAdmissionError
from src.interface.ui.ui_delete_window import Ui_DeleteWindow
from src.main.settings import MAIN_WINDOW_ICON


class DeleteWindow(QDialog):
    submitted_delete = Signal(str, str, date, date, str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_DeleteWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(MAIN_WINDOW_ICON))
        self.setWindowTitle("Удаление записей")
        self.__add_functions()

        self.__data_saver = DataSaver(
            self.ui.line_edit_fio_user,
            self.ui.line_edit_address,
            self.ui.line_edit_date_of_birthday,
            self.ui.line_edit_date_of_admission,
            self.ui.line_edit_doctor,
        )

    def __add_functions(self) -> None:
        self.ui.button_delete.clicked.connect(lambda: self.__save_data())
        self.ui.button_cancel.clicked.connect(lambda: self.close())

    def __save_data(self) -> None:
        try:
            fio_user, address, birthday, date_of_admission, fio_doctor = self.__data_saver.save_data()
            self.submitted_delete.emit(fio_user, address, birthday, date_of_admission, fio_doctor)
        except Exception as e:
            pass
