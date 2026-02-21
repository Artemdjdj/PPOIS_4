import sys
from datetime import date
from typing import List
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QDialog
from PySide6.QtGui import QIcon

from src.main.paginator import Paginator
from src.exceptions.exceptions import BirthdayError, DateOfAdmissionError
from src.interface.ui.ui_search_window import Ui_SearchWindow
from src.main.settings import MAIN_WINDOW_ICON
from src.main.utils import DateConverter
from src.db.models.clinic import ClinicInfoBase
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
        self.__paginator = self.__paginator = Paginator(self.ui.button_prev, self.ui.button_first, self.ui.button_current,
                                     self.ui.button_last, self.ui.button_next, self.ui.comboBox_pagination,
                                     self.ui.table_of_recording)


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
        self.__records = []


    def __add_functions(self) -> None:
        self.ui.button_search.clicked.connect(lambda: self.__save_data())
        self.ui.button_cancel.clicked.connect(lambda: self.close())
        self.ui.button_prev.clicked.connect(lambda: self.__get_special_page(self.__paginator.current_page - 1))
        self.ui.button_next.clicked.connect(lambda: self.__get_special_page(self.__paginator.current_page + 1))
        self.ui.button_first.clicked.connect(lambda: self.__get_special_page(1))
        self.ui.button_last.clicked.connect(lambda: self.__get_special_page(self.__paginator.count_pages))
        self.ui.comboBox_pagination.currentIndexChanged.connect(lambda: self.__change_count_pages())

    def __get_special_page(self, new_current_page: int) -> None:
        self.__paginator.current_page = new_current_page
        self.load_data_to_table()

    def __change_count_pages(self) -> None:
        self.__paginator.start_pagination()
        self.load_data_to_table()

    def set_records(self, records: List[ClinicInfoBase]) -> None:
        self.__paginator.start_pagination()
        self.__records = records
        self.load_data_to_table()

    def load_data_to_table(self) -> None:
        records = self.__paginator.get_data_from_page(self.__records)
        self.__table_recorder.record(records)

    def __save_data(self) -> None:
        try:
            self.ui.tab_widget_footer.setCurrentWidget(self.ui.tab_pagination)
            fio_user, address, birthday, date_of_admission, fio_doctor = self.__data_saver.save_data()
            self.submitted_search.emit(fio_user, address, birthday, date_of_admission, fio_doctor)
        except Exception as e:
            pass
