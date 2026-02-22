import xml.sax as sax
from datetime import date
from typing import Optional, List
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QPixmap

from data_processing.data_manager.loader import XMLLoader
from src.data_processing.data_manager.saver import XMLSaver
from src.controllers.after_delete_clinic_info import AfterDeleteWindow
from src.controllers.confirm_delete_clinic_info import ConfirmWindow
from src.controllers.delete_clinic_info import DeleteWindow
from src.controllers.save_clinic_info import SaveWindow
from src.controllers.confirmation_to_db import ConfirmToDbWindow
from src.main.paginator import PaginationMixin
from src.main.settings import image_delete_successful, stylesheet_for_not_visible_button, stylesheet_for_button_save_to_db
from src.controllers.search_clinic_info import SearchWindow
from data_processing.db.models.clinic import ClinicInfoBase
from data_processing.db.clinic_info_service import ClinicInfoService
from data_processing.db.db_manager import DatabaseManager
from src.interface.ui.ui_main_window import Ui_MainWindow
from src.controllers.add_clinic_info import AddingDataWindow
from src.main.settings import MAIN_WINDOW_ICON
from src.main.settings import label_delete_nothing_text, image_delete_nothing


class MainWindow(PaginationMixin, QMainWindow):
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
        self.__clinic_info_service: ClinicInfoService = ClinicInfoService(DatabaseManager())
        # пагинация
        # self.__current_page: Optional[int] = None
        # self.__count_pages: Optional[int] = None
        # self.__count_of_records_on_page: Optional[int] = None
        self._records: Optional[List[ClinicInfoBase]] = []
        self.__is_work_in_db: bool = False

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
            self.ui.tab_pagination
        )

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
        self.ui.button_load_from_file.clicked.connect(lambda: self.__load_data_from_xml())
        self.ui.button_save_to_db.clicked.connect(lambda: self.__save_to_db())
        self.ui.button_add_new_record.clicked.connect(
            lambda: self.__create_new_clinic_info()
        )
        self._connect_pagination_buttons()
        self.ui.button_search.clicked.connect(lambda: self.__search_records())
        self.ui.button_delete.clicked.connect(lambda: self.__delete_records())
        self.ui.button_show_tree.clicked.connect(lambda: self.__view_as_tree())
        self.ui.button_back_to_table.clicked.connect(lambda: self.__back_to_table())
        self.ui.button_exit_app.clicked.connect(lambda: self.__save_data_into_file())
        self.ui.button_back.clicked.connect(lambda: self.__back_to_choose_data())

    def __start_app(self) -> None:
        self.ui.tab_widget_main.setCurrentWidget(self.ui.tab_main_page)

    def __exit(self) -> None:
        self.close()

    def __back_to_choose_data(self)->None:
        self.ui.tab_widget_work_state.setCurrentWidget(self.ui.tab_load_data)
        self.ui.tab_widget_footer.setCurrentWidget(self.ui.tab_footer)
        self.ui.tab_widget_records.setCurrentWidget(self.ui.tab_no_records)
        self.ui.tab_widget_header.setCurrentWidget(self.ui.tab_header_other)

    def __base_settings_to_show_data(self)->None:
        self._paginator.start_pagination()
        self._load_data_to_table()
        self.ui.tab_widget_work_state.setCurrentWidget(self.ui.tab_work_with_data)
        self.ui.tab_widget_footer.setCurrentWidget(self.ui.tab_pagination)
        self.ui.tab_widget_header.setCurrentWidget(self.ui.tab_header_search)

    def __load_data_from_db(self) -> None:
        self.__is_work_in_db = True
        self.ui.button_save_to_db.setStyleSheet(stylesheet_for_not_visible_button)
        self.ui.button_save_to_db.setEnabled(False)
        self.ui.button_save_to_db.setText("")
        self._records = self.__clinic_info_service.get_all_records_clinic_info()
        self.__base_settings_to_show_data()

    def __load_data_from_xml(self)->None:
        self.__is_work_in_db = False
        self.ui.button_save_to_db.setStyleSheet(stylesheet_for_button_save_to_db)
        self.ui.button_save_to_db.setEnabled(True)
        self.ui.button_save_to_db.setText("Загрузить \n в бд")
        self._records = self.__choose_load_file()
        if self._records is not None:
            self.__base_settings_to_show_data()

    def __choose_load_file(self) -> Optional[List[ClinicInfoBase]]:
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Открыть файл",
            "",
            "XML Files (*.xml);;All Files (*)"
        )
        if not filename:
            return None

        try:
            loader = XMLLoader(filename)
            records = loader.load()
            return records
        except sax.SAXParseException as e:
            QMessageBox.critical(self, "Ошибка XML", f"Файл повреждён или неверный формат:\n{e}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть файл или структура данных файле нарушена:\n{e}")
        return None

    def __add_new_clinic_info(
            self,
            fio_user: Optional[str],
            address: Optional[str],
            birthday: Optional[date],
            date_of_admission: Optional[date],
            fio_doctor: Optional[str],
            conclusion: Optional[str],
    ) -> None:
        if fio_user is not None:
            clinic_info = ClinicInfoBase(
                fio_patient=fio_user,
                address=address,
                birthday=birthday,
                date_of_admission=date_of_admission,
                fio_doctor=fio_doctor,
                conclusion=conclusion,
            )
            if self.__is_work_in_db:
                self.__clinic_info_service.create_clinic_info(clinic_info)
                self.__load_data_from_db()
            else:
                self._records.append(clinic_info)
                self.__base_settings_to_show_data()

    def __create_new_clinic_info(self) -> None:
        dialog = AddingDataWindow()
        dialog.submitted.connect(self.__add_new_clinic_info)
        dialog.exec()

    def __search_records(self) -> None:
        self.__dialog = SearchWindow()
        self.__dialog.submitted_search.connect(self.__load_filter_records_to_search)
        self.__dialog.exec()

    def __filter_records(
            self, fio_user, address, birthday, date_of_admission, fio_doctor
    ) -> list[ClinicInfoBase]:

        all_records = self.__clinic_info_service.get_all_records_clinic_info() if self.__is_work_in_db else self._records
        if fio_user:
            all_records = [r for r in all_records if r.fio_patient == fio_user]
        if address:
            all_records = [r for r in all_records if r.address == address]
        if birthday:
            all_records = [r for r in all_records if r.birthday == birthday]
        if date_of_admission:
            all_records = [
                r for r in all_records if r.date_of_admission == date_of_admission
            ]
        if fio_doctor:
            all_records = [r for r in all_records if r.fio_doctor == fio_doctor]
        return all_records

    def __load_filter_records_to_search(
            self, fio_user, address, birthday, date_of_admission, fio_doctor
    ) -> None:
        all_records = self.__filter_records(
            fio_user, address, birthday, date_of_admission, fio_doctor
        )
        self.__dialog.set_records(all_records)

    def __delete_records(self) -> None:
        if len(self._records)>0:
            self.__dialog_del = DeleteWindow()
            self.__dialog_del.submitted_delete.connect(self.__delete_records_in_main)
            self.__dialog_del.exec()
        else:
            self.__create_after_delete_window(is_success=False)
            self.__after_delete_dialog.exec()

    def __create_after_delete_window(
            self, is_success: bool, count_of_delete_records: int = 0
    ) -> None:
        self.__after_delete_dialog = AfterDeleteWindow()
        if not is_success:
            self.__after_delete_dialog.ui.label_after_delete_message.setText(
                label_delete_nothing_text
            )
            self.__after_delete_dialog.ui.label_after_delete.setPixmap(
                QPixmap(image_delete_nothing)
            )
        else:
            self.__after_delete_dialog.ui.label_after_delete_message.setText(
                f"Успешно удалено {count_of_delete_records} элементов!"
            )
            self.__after_delete_dialog.ui.label_after_delete.setPixmap(
                QPixmap(image_delete_successful)
            )

    def __delete_records_in_main(
            self, fio_user, address, birthday, date_of_admission, fio_doctor
    ) -> None:
        all_records = self.__filter_records(
            fio_user, address, birthday, date_of_admission, fio_doctor
        )
        if len(all_records) == 0:
            self.__create_after_delete_window(is_success=False)
            self.__after_delete_dialog.exec()
        else:
            self.__confirm_dialog = ConfirmWindow()
            self.__confirm_dialog.delete.connect(
                lambda confirmed: self.__on_delete_result(confirmed, all_records)
            )
            self.__confirm_dialog.exec()

    def __on_delete_result(
            self, confirmed: bool, records: List[ClinicInfoBase]
    ) -> None:
        if confirmed:
            if self.__is_work_in_db:
                self.__clinic_info_service.delete_records_clinic_info(records)
            else:
                self._records = [r for r in self._records if r not in records]
            self.__create_after_delete_window(
                is_success=True, count_of_delete_records=len(records)
            )
            self.__after_delete_dialog.exec()
            if self.__is_work_in_db:
                self.__load_data_from_db()
            else:
                self._load_data_to_table()
        else:
            self.__create_after_delete_window(is_success=False)
            self.__after_delete_dialog.exec()
        if self.__dialog_del:
            self.__dialog_del.close()

    def __view_as_tree(self):

        self.ui.tab_widget_records.setCurrentWidget(self.ui.tab_tree_of_records)
        self.ui.tab_widget_footer.setCurrentWidget(self.ui.tab_footer)
        tree = self.ui.treeWidget
        tree.clear()
        tree.setHeaderLabel("")

        for name, record in enumerate(self._records):
            item = QTreeWidgetItem(tree)
            item.setText(0, f"Запись номер: {name + 1}")

            child = QTreeWidgetItem(item)
            child.setText(0, f"ФИО пациента: {record.fio_patient}")
            child2 = QTreeWidgetItem(item)
            child2.setText(0, f"Адрес пациента: {record.address}")
            child3 = QTreeWidgetItem(item)
            child3.setText(0, f"Дата рождения: {record.birthday}")
            child4 = QTreeWidgetItem(item)
            child4.setText(0, f"Дата приема: {record.date_of_admission}")
            child5 = QTreeWidgetItem(item)
            child5.setText(0, f"ФИО доктора: {record.fio_doctor}")

    def __back_to_table(self) -> None:
        self.ui.tab_widget_records.setCurrentWidget(self.ui.tab_list_of_records)
        self.ui.tab_widget_footer.setCurrentWidget(self.ui.tab_pagination)

    def __save_data_into_file(self) -> None:
        self.__dialog_save = SaveWindow()
        self.__dialog_save.cancel.connect(lambda save: self.__result_save(save))
        self.__dialog_save.exec()

    def __result_save(self, save: bool) -> None:
        if save:
            filename, _ = QFileDialog.getSaveFileName(
                self,
                "Сохранить файл",
                "",
                "XML Files (*.xml);;All Files (*)"
            )
            if not filename:
                return

            if not filename.endswith(".xml"):
                filename += ".xml"

            try:
                saver = XMLSaver(filename, self._records)
                saver.save()
                QMessageBox.information(self, "Успех", f"Файл сохранён:\n{filename}")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл:\n{e}")

        self.__exit()

    def __save_to_db(self) -> None:
        self.__dialog_confirm_to_save = ConfirmToDbWindow()
        self.__dialog_confirm_to_save.confirm_to_db.connect(lambda confirmed: self.__on_save_confirm_to_save(confirmed))
        self.__dialog_confirm_to_save.exec()

    def __on_save_confirm_to_save(self, confirmed: bool) -> None:
        if confirmed:
            try:
                self.__clinic_info_service.save_new_clinic_info(self._records)
                QMessageBox.information(self, "Успех", f"Данные успешно занесены в базу данных!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось занести данные в базу данных")


