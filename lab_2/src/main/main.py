import sys
from datetime import date
from typing import Optional, List
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton
from PySide6.QtGui import QIcon
from src.db.models.clinic import ClinicInfoBase
from src.db.clinic_info_service import ClinicInfoService
from src.db.db_manager import DatabaseManager
from src.interface.ui.ui_main_window import Ui_MainWindow
from src.main.add_clinic_info import AddingDataWindow
from src.main.settings import MAIN_WINDOW_ICON
from src.main.settings import stylesheet_for_page_in_pagination, stylesheet_for_not_visible_button, stylesheet_for_active_page_in_pagination


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(MAIN_WINDOW_ICON))
        self.setWindowTitle("Медицинское приложение для учета обслуживаний пациентов")
        # подключение обработчиков
        self.__add_functions()
        # стартовая настройка виджетов
        self.__basic_settings_with_tabs()
        self.__clinic_info_service = ClinicInfoService(DatabaseManager())
        # пагинация
        self.__current_page:Optional[int] = None
        self.__count_pages:Optional[int] = None
        self.__count_of_records_on_page:Optional[int] = None
        self.__records:List[ClinicInfoBase] = []

    def __basic_settings_with_tabs(self) -> None:
        self.ui.tab_widget_main.setCurrentWidget(self.ui.tab_start_page)
        self.ui.tab_widget_header.setCurrentWidget(self.ui.tab_header_other)
        self.ui.tab_widget_footer.setCurrentWidget(self.ui.tab_footer)
        self.ui.tab_widget_records.setCurrentWidget(self.ui.tab_no_records)
        self.ui.tab_widget_work_state.setCurrentWidget(self.ui.tab_load_data)

    def __add_functions(self) -> None:
        self.ui.button_start.clicked.connect(lambda: self.__start_app())
        self.ui.button_exit.clicked.connect(lambda: self.__exit())
        self.ui.button_load_from_db.clicked.connect(lambda: self.__load_data_from_db())
        self.ui.button_add_new_record.clicked.connect(lambda: self.__create_new_clinic_info())
        self.ui.button_prev.clicked.connect(lambda: self.__get_special_page(self.__current_page-1))
        self.ui.button_next.clicked.connect(lambda: self.__get_special_page(self.__current_page+1))
        self.ui.button_first.clicked.connect(lambda: self.__get_special_page(1))
        self.ui.button_last.clicked.connect(lambda: self.__get_special_page(self.__count_pages))
        self.ui.comboBox_pagination.currentIndexChanged.connect(lambda: self.__change_count_pages())

    def __start_app(self) -> None:
        # переключение на новый tab
        self.ui.tab_widget_main.setCurrentWidget(self.ui.tab_main_page)

    def __exit(self) -> None:
        self.close()

    def __start_pagination(self)->None:
        self.__count_pages = None
        self.__count_of_records_on_page = None
        self.__current_page = None

    def __change_count_pages(self)->None:
        self.__start_pagination()
        self.__load_from_db_to_table()

    def __load_data_from_db(self)->None:
        self.__start_pagination()
        self.__records = self.__clinic_info_service.get_all_records_clinic_info()
        self.__load_from_db_to_table()

    def __load_from_db_to_table(self) -> None:
        self.__create_pagination()
        left_border = (self.__current_page-1)*self.__count_of_records_on_page
        right_border = self.__current_page*self.__count_of_records_on_page if self.__current_page*self.__count_of_records_on_page < len(self.__records) else len(self.__records)
        print(f"\n левая граница: {left_border},  правая граница: {right_border}")
        records = self.__records[left_border:right_border]
        if records and len(records) > 0:
            self.ui.table_of_recording.clear()
            self.ui.tab_widget_records.setCurrentWidget(self.ui.tab_list_of_records)
            for row, record in enumerate(records):
                self.ui.table_of_recording.setItem(row, 0, QTableWidgetItem(str(record.fio_patient)))
                self.ui.table_of_recording.setItem(row, 1, QTableWidgetItem(str(record.address)))
                self.ui.table_of_recording.setItem(row, 2, QTableWidgetItem(str(record.birthday)))
                self.ui.table_of_recording.setItem(row, 3, QTableWidgetItem(str(record.date_of_admission)))
                self.ui.table_of_recording.setItem(row, 4, QTableWidgetItem(str(record.fio_doctor)))
                self.ui.table_of_recording.setItem(row, 5, QTableWidgetItem(str(record.conclusion)))
        self.ui.tab_widget_work_state.setCurrentWidget(self.ui.tab_work_with_data)
        self.ui.tab_widget_footer.setCurrentWidget(self.ui.tab_pagination)

    def __add_new_clinic_info(self, fio_user: Optional[str], address: Optional[str], birthday: Optional[date],
                              date_of_admission: Optional[date], fio_doctor: Optional[str],
                              conclusion: Optional[str]) -> None:
        if fio_user is not None:
            clinic_info = ClinicInfoBase(fio_patient=fio_user,
                                         address=address,
                                         birthday=birthday,
                                         date_of_admission=date_of_admission,
                                         fio_doctor=fio_doctor,
                                         conclusion=conclusion)
            self.__clinic_info_service.create_clinic_info(clinic_info)
            self.__load_data_from_db()

    def __create_new_clinic_info(self) -> None:
        dialog = AddingDataWindow()
        dialog.submitted.connect(self.__add_new_clinic_info)
        dialog.exec()

    def __create_pagination(self) -> None:
        if self.__count_pages is None:
            self.__count_of_records_on_page = count_records_on_page = int(self.ui.comboBox_pagination.currentText())
            self.ui.table_of_recording.setRowCount(self.__count_of_records_on_page)
            print(f" количество записей на странице: {self.__count_of_records_on_page}")
            count_records = len(self.__records)
            temp_count_pages = count_records//count_records_on_page
            remainder = count_records/count_records_on_page - temp_count_pages
            self.__count_pages = temp_count_pages if remainder == 0 else temp_count_pages+1
            print(f" количество страниц: {self.__count_pages}")
            self.__current_page = 1
        self.__paginate()

    def __get_special_page(self, new_current_page:int) -> None:
        self.__current_page = new_current_page
        self.__load_from_db_to_table()

    def __apply_style_to_button(self, button:QPushButton, style:str=stylesheet_for_not_visible_button, enabled:bool=False, text:str="")->None:
        button.setStyleSheet(style)
        button.setEnabled(enabled)
        button.setText(text)

    def __paginate(self):
        if self.__count_pages == 1:
            self.__apply_style_to_button(self.ui.button_prev)
            self.__apply_style_to_button(self.ui.button_next)
            self.__apply_style_to_button(self.ui.button_first)
            self.__apply_style_to_button(self.ui.button_last)
        elif self.__count_pages >1:
            if self.__current_page == 1:
                self.__apply_style_to_button(self.ui.button_prev)
                self.__apply_style_to_button(self.ui.button_first)
                self.__apply_style_to_button(self.ui.button_last, style=stylesheet_for_page_in_pagination,enabled=True, text=f"{self.__count_pages}")
                self.__apply_style_to_button(self.ui.button_next, style=stylesheet_for_page_in_pagination,enabled=True, text=">")
            elif self.__current_page == self.__count_pages:
                self.__apply_style_to_button(self.ui.button_prev, style=stylesheet_for_page_in_pagination, enabled=True, text="<")
                self.__apply_style_to_button(self.ui.button_first, style=stylesheet_for_page_in_pagination,enabled=True, text="1")
                self.__apply_style_to_button(self.ui.button_last)
                self.__apply_style_to_button(self.ui.button_next)
            else:
                self.__apply_style_to_button(self.ui.button_prev, style=stylesheet_for_page_in_pagination, enabled=True, text="<")
                self.__apply_style_to_button(self.ui.button_next, style=stylesheet_for_page_in_pagination, enabled=True, text=">")
                self.__apply_style_to_button(self.ui.button_first, style=stylesheet_for_page_in_pagination,enabled=True, text="1")
                self.__apply_style_to_button(self.ui.button_last, style=stylesheet_for_page_in_pagination,enabled=True, text=f"{self.__count_pages}")
                self.__apply_style_to_button(self.ui.button_current,style=stylesheet_for_active_page_in_pagination, enabled=True)
        self.__apply_style_to_button(self.ui.button_current, style=stylesheet_for_active_page_in_pagination,
                                       enabled=True, text=f"{self.__current_page}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())