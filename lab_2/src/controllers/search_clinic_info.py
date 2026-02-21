import sys
from datetime import date
from typing import List
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QDialog
from PySide6.QtGui import QIcon
from src.exceptions.exceptions import BirthdayError, DateOfAdmissionError
from src.interface.ui.ui_search_window import Ui_SearchWindow
from src.main.settings import MAIN_WINDOW_ICON
from src.main.utils import DateConverter
from src.db.models.clinic import ClinicInfoBase
from src.validator.fio_validator import FioUserValidator, FioDoctorValidator
from src.validator.date_validator import DateValidator
from src.validator.address_validator import BelarusAddressValidator
from src.exceptions.exceptions import FioUserError, FioDoctorError, DateError, AddressError
from src.main.table_recorder import TableRecorder
from src.main.data_saver import DataSaver

class SearchWindow(QDialog):
    submitted_search = Signal(str, str, date, date, str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(MAIN_WINDOW_ICON))
        self.setWindowTitle("Поиск записей")
        self.__add_functions()

        self.__table_recorder = TableRecorder(
            self.ui.table_of_recording,
            self.ui.tab_widget_records,
            self.ui.tab_list_of_records,
            self.ui.tab_no_records
        )
        self.__data_saver = DataSaver(
            self.ui.line_edit_fio_user,
            self.ui.line_edit_address,
            self.ui.line_edit_date_of_birthday,
            self.ui.line_edit_date_of_admission,
            self.ui.line_edit_doctor,
        )


    def __add_functions(self) -> None:
        self.ui.button_search.clicked.connect(lambda: self.__save_data())
        self.ui.button_cancel.clicked.connect(lambda: self.close())

    def load_data_to_table(self, records: List[ClinicInfoBase]) -> None:
        self.ui.table_of_recording.setRowCount(len(records))
        self.__table_recorder.record(records)

    def __save_data(self) -> None:
        try:
            fio_user, address, birthday, date_of_admission, fio_doctor = self.__data_saver.save_data()
            self.submitted_search.emit(fio_user, address, birthday, date_of_admission, fio_doctor)
        except Exception as e:
            pass
