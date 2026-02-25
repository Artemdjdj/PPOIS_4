from datetime import date
from typing import List
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QIcon

from src.main.paginator import PaginationMixin
from src.interface.ui.ui_search_window import Ui_SearchWindow
from src.main.settings import MAIN_WINDOW_ICON
from src.data_processing.db.models.clinic import ClinicInfoBase
from src.main.data_saver import DataSaver


class SearchWindow(PaginationMixin, QDialog):
    submitted_search = Signal(str, str, date, date, str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(MAIN_WINDOW_ICON))
        self.setWindowTitle("Поиск записей")
        self._records = []
        self._init_paginator(
            self.ui.button_prev,
            self.ui.button_first,
            self.ui.button_current,
            self.ui.button_last,
            self.ui.button_next,
            self.ui.comboBox_pagination,
            self.ui.table_of_recording,
        )
        self._init_table_recorder(
            self.ui.table_of_recording,
            self.ui.tab_widget_records,
            self.ui.tab_list_of_records,
            self.ui.tab_no_records,
            self.ui.tab_widget_footer,
            self.ui.tab_footer,
            self.ui.tab_pagination,
        )
        self.__data_saver = DataSaver(
            self.ui.line_edit_fio_user,
            self.ui.line_edit_address,
            self.ui.line_edit_date_of_birthday,
            self.ui.line_edit_date_of_admission,
            self.ui.line_edit_doctor,
        )
        self.__add_functions()

    def set_records(self, records: List[ClinicInfoBase]) -> None:
        self._paginator.start_pagination()
        self._records = records
        self._load_data_to_table()
        if len(self._records)>0:
            QMessageBox.information(self, "Найденные записи", f"Количество найденных записей: {len(self._records)}")
        else:
            QMessageBox.critical(self, "Ничего не найдено", f"Возможно вы ошиблись при вводе данных")

    def __add_functions(self) -> None:
        self._connect_pagination_buttons()
        self.ui.button_search.clicked.connect(self.__save_data)
        self.ui.button_cancel.clicked.connect(self.close)

    def __save_data(self) -> None:
        try:
            fio_user, address, birthday, date_of_admission, fio_doctor = (
                self.__data_saver.save_data()
            )
            self.submitted_search.emit(
                fio_user, address, birthday, date_of_admission, fio_doctor
            )

        except Exception as e:
            self.ui.tab_widget_records.setCurrentWidget(self.ui.tab_no_records)
            self.ui.tab_widget_footer.setCurrentWidget(self.ui.tab_footer)
            QMessageBox.critical(
                self, "Ошибка", f"{e}"
            )
