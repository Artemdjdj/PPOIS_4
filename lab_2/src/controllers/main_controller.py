import sys
from datetime import date
from typing import Optional, List
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtGui import QIcon, QPixmap

from controllers.after_delete_clinic_info import AfterDeleteWindow
from controllers.confirm_delete_clinic_info import ConfirmWindow
from controllers.delete_clinic_info import DeleteWindow
from src.main.paginator import Paginator
from src.main.settings import image_delete_successful
from controllers.search_clinic_info import SearchWindow
from src.db.models.clinic import ClinicInfoBase
from src.db.clinic_info_service import ClinicInfoService
from src.db.db_manager import DatabaseManager
from src.interface.ui.ui_main_window import Ui_MainWindow
from controllers.add_clinic_info import AddingDataWindow
from src.main.settings import MAIN_WINDOW_ICON
from src.main.settings import stylesheet_for_page_in_pagination, stylesheet_for_not_visible_button, \
    stylesheet_for_active_page_in_pagination
from src.main.settings import label_delete_nothing_text, image_delete_nothing
from src.main.table_recorder import TableRecorder


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
        # self.__current_page: Optional[int] = None
        # self.__count_pages: Optional[int] = None
        # self.__count_of_records_on_page: Optional[int] = None
        self.__records: List[ClinicInfoBase] = []
        self.__table_recorder = TableRecorder(
            self.ui.table_of_recording,
            self.ui.tab_widget_records,
            self.ui.tab_list_of_records,
            self.ui.tab_no_records
        )
        self.__paginator = Paginator(self.ui.button_prev, self.ui.button_first, self.ui.button_current,
                                     self.ui.button_last, self.ui.button_next, self.ui.comboBox_pagination,
                                     self.ui.table_of_recording)

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
        self.ui.button_prev.clicked.connect(lambda: self.__get_special_page(self.__paginator.current_page - 1))
        self.ui.button_next.clicked.connect(lambda: self.__get_special_page(self.__paginator.current_page + 1))
        self.ui.button_first.clicked.connect(lambda: self.__get_special_page(1))
        self.ui.button_last.clicked.connect(lambda: self.__get_special_page(self.__paginator.count_pages))
        self.ui.comboBox_pagination.currentIndexChanged.connect(lambda: self.__change_count_pages())
        self.ui.button_search.clicked.connect(lambda: self.__search_records())
        self.ui.button_delete.clicked.connect(lambda: self.__delete_records())

    def __start_app(self) -> None:
        # переключение на новый tab
        self.ui.tab_widget_main.setCurrentWidget(self.ui.tab_main_page)

    def __exit(self) -> None:
        self.close()

    # def __start_pagination(self) -> None:
    #     self.__count_pages = None
    #     self.__count_of_records_on_page = None
    #     self.__current_page = None

    def __change_count_pages(self) -> None:
        self.__paginator.start_pagination()
        self.__load_from_db_to_table()

    def __load_data_from_db(self) -> None:
        self.__paginator.start_pagination()
        self.__records = self.__clinic_info_service.get_all_records_clinic_info()
        self.__load_from_db_to_table()

    def __load_from_db_to_table(self) -> None:
        self.__paginator.create_pagination(self.__records)
        left_border = (self.__paginator.current_page - 1) * self.__paginator.count_of_records_on_page
        right_border = self.__paginator.current_page * self.__paginator.count_of_records_on_page if self.__paginator.current_page * self.__paginator.count_of_records_on_page < len(
            self.__records) else len(self.__records)
        print(f"\n левая граница: {left_border},  правая граница: {right_border}")
        records = self.__records[left_border:right_border]
        self.__table_recorder.record(records)
        self.ui.tab_widget_work_state.setCurrentWidget(self.ui.tab_work_with_data)
        self.ui.tab_widget_footer.setCurrentWidget(self.ui.tab_pagination)
        self.ui.tab_widget_header.setCurrentWidget(self.ui.tab_header_search)

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
            # self.__records.append(clinic_info)
            # self.__start_pagination()
            # self.__load_from_db_to_table()
            self.__clinic_info_service.create_clinic_info(clinic_info)
            self.__load_data_from_db()

    def __create_new_clinic_info(self) -> None:
        dialog = AddingDataWindow()
        dialog.submitted.connect(self.__add_new_clinic_info)
        dialog.exec()

    # def __create_pagination(self) -> None:
    #     if self.__count_pages is None:
    #         self.__count_of_records_on_page = count_records_on_page = int(self.ui.comboBox_pagination.currentText())
    #         self.ui.table_of_recording.setRowCount(self.__count_of_records_on_page)
    #         print(f" количество записей на странице: {self.__count_of_records_on_page}")
    #         count_records = len(self.__records)
    #         temp_count_pages = count_records // count_records_on_page
    #         remainder = count_records / count_records_on_page - temp_count_pages
    #         self.__count_pages = temp_count_pages if remainder == 0 else temp_count_pages + 1
    #         print(f" количество страниц: {self.__count_pages}")
    #         self.__current_page = 1
    #     self.__paginate()

    def __get_special_page(self, new_current_page: int) -> None:
        self.__paginator.current_page = new_current_page
        self.__load_from_db_to_table()

    # def __apply_style_to_button(self, button: QPushButton, style: str = stylesheet_for_not_visible_button,
    #                             enabled: bool = False, text: str = "") -> None:
    #     button.setStyleSheet(style)
    #     button.setEnabled(enabled)
    #     button.setText(text)

    # def __paginate(self):
    #     if self.__count_pages == 1:
    #         self.__apply_style_to_button(self.ui.button_prev)
    #         self.__apply_style_to_button(self.ui.button_next)
    #         self.__apply_style_to_button(self.ui.button_first)
    #         self.__apply_style_to_button(self.ui.button_last)
    #     elif self.__count_pages > 1:
    #         if self.__current_page == 1:
    #             self.__apply_style_to_button(self.ui.button_prev)
    #             self.__apply_style_to_button(self.ui.button_first)
    #             self.__apply_style_to_button(self.ui.button_last, style=stylesheet_for_page_in_pagination, enabled=True,
    #                                          text=f"{self.__count_pages}")
    #             self.__apply_style_to_button(self.ui.button_next, style=stylesheet_for_page_in_pagination, enabled=True,
    #                                          text=">")
    #         elif self.__current_page == self.__count_pages:
    #             self.__apply_style_to_button(self.ui.button_prev, style=stylesheet_for_page_in_pagination, enabled=True,
    #                                          text="<")
    #             self.__apply_style_to_button(self.ui.button_first, style=stylesheet_for_page_in_pagination,
    #                                          enabled=True, text="1")
    #             self.__apply_style_to_button(self.ui.button_last)
    #             self.__apply_style_to_button(self.ui.button_next)
    #         else:
    #             self.__apply_style_to_button(self.ui.button_prev, style=stylesheet_for_page_in_pagination, enabled=True,
    #                                          text="<")
    #             self.__apply_style_to_button(self.ui.button_next, style=stylesheet_for_page_in_pagination, enabled=True,
    #                                          text=">")
    #             self.__apply_style_to_button(self.ui.button_first, style=stylesheet_for_page_in_pagination,
    #                                          enabled=True, text="1")
    #             self.__apply_style_to_button(self.ui.button_last, style=stylesheet_for_page_in_pagination, enabled=True,
    #                                          text=f"{self.__count_pages}")
    #             self.__apply_style_to_button(self.ui.button_current, style=stylesheet_for_active_page_in_pagination,
    #                                          enabled=True)
    #     self.__apply_style_to_button(self.ui.button_current, style=stylesheet_for_active_page_in_pagination,
    #                                  enabled=True, text=f"{self.__current_page}")

    def __search_records(self) -> None:
        self.__dialog = SearchWindow()
        self.__dialog.submitted_search.connect(self.__load_filter_records_to_search)
        self.__dialog.exec()

    def __filter_records(self, fio_user, address, birthday, date_of_admission, fio_doctor) -> list[ClinicInfoBase]:
        all_records = self.__clinic_info_service.get_all_records_clinic_info()
        if fio_user:
            all_records = [r for r in all_records if r.fio_patient == fio_user]
        if address:
            all_records = [r for r in all_records if r.address == address]
        if birthday:
            all_records = [r for r in all_records if r.birthday == birthday]
        if date_of_admission:
            all_records = [r for r in all_records if r.date_of_admission == date_of_admission]
        if fio_doctor:
            all_records = [r for r in all_records if r.fio_doctor == fio_doctor]
        return all_records

    def __load_filter_records_to_search(self, fio_user, address, birthday, date_of_admission, fio_doctor) -> None:
        all_records = self.__filter_records(fio_user, address, birthday, date_of_admission, fio_doctor)
        self.__dialog.load_data_to_table(all_records)

    def __delete_records(self) -> None:
        self.__dialog = DeleteWindow()
        self.__dialog.submitted_delete.connect(self.__delete_records_in_main)
        self.__dialog.exec()

    def __create_after_delete_window(self, is_success: bool, count_of_delete_records: int = 0) -> None:
        self.__after_delete_dialog = AfterDeleteWindow()
        if not is_success:
            self.__after_delete_dialog.ui.label_after_delete_message.setText(label_delete_nothing_text)
            self.__after_delete_dialog.ui.label_after_delete.setPixmap(QPixmap(image_delete_nothing))
        else:
            self.__after_delete_dialog.ui.label_after_delete_message.setText(
                f"Успешно удалено {count_of_delete_records} элементов!")
            self.__after_delete_dialog.ui.label_after_delete.setPixmap(QPixmap(image_delete_successful))

    def __delete_records_in_main(self, fio_user, address, birthday, date_of_admission, fio_doctor) -> None:
        all_records = self.__filter_records(fio_user, address, birthday, date_of_admission, fio_doctor)
        if len(all_records) == 0:
            self.__create_after_delete_window(is_success=False)
            self.__after_delete_dialog.exec()
        else:
            self.__confirm_dialog = ConfirmWindow()
            self.__confirm_dialog.delete.connect(
                lambda confirmed: self.__on_delete_result(confirmed, all_records)
            )
            self.__confirm_dialog.exec()

    def __on_delete_result(self, confirmed: bool, records: List[ClinicInfoBase]) -> None:
        if confirmed:
            self.__clinic_info_service.delete_records_clinic_info(records)
            # records_remove_ids = set(r.id for r in records)
            # self.__records = [r for r in self.__records if r.id not in records_remove_ids]
            self.__create_after_delete_window(is_success=True, count_of_delete_records=len(records))
            self.__after_delete_dialog.exec()
            self.__load_data_from_db()
        else:
            self.__create_after_delete_window(is_success=False)
            self.__after_delete_dialog.exec()
