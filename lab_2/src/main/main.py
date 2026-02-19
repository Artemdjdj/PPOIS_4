import sys
from typing import Optional

from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PySide6.QtGui import QIcon

from src.db.models.clinic import ClinicInfoBase
from src.db.clinic_info_service import ClinicInfoService
from src.db.db_manager import DatabaseManager
from src.interface.ui.ui_main_window import Ui_MainWindow
from src.main.add_clinic_info import AddingDataWindow
from src.main.settings import MAIN_WINDOW_ICON


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

    def __basic_settings_with_tabs(self) -> None:
        self.ui.tab_widget_main.setCurrentWidget(self.ui.tab_start_page)
        self.ui.tab_widget_header.setCurrentWidget(self.ui.tab_header_other)
        self.ui.tab_widget_footer.setCurrentWidget(self.ui.tab_footer)
        self.ui.tab_widget_records.setCurrentWidget(self.ui.tab_no_records)
        self.ui.tab_widget_work_state.setCurrentWidget(self.ui.tab_load_data)

    def __add_functions(self) -> None:
        self.ui.button_start.clicked.connect(lambda: self.__start_app())
        self.ui.button_exit.clicked.connect(lambda: self.__exit())
        self.ui.button_load_from_db.clicked.connect(lambda: self.__load_from_db())
        self.ui.button_add_new_record.clicked.connect(lambda: self.__create_new_clinic_info())

    def __start_app(self) -> None:
        # переключение на новый tab
        self.ui.tab_widget_main.setCurrentWidget(self.ui.tab_main_page)

    def __exit(self) -> None:
        self.close()

    def __load_from_db(self) -> None:
        records = self.__clinic_info_service.get_all_records_clinic_info()
        if records and len(records) > 0:
            self.ui.tab_widget_records.setCurrentWidget(self.ui.tab_list_of_records)
            for row, record in enumerate(records):
                self.ui.table_of_recording.setItem(row, 0, QTableWidgetItem(str(record.fio_patient)))
                self.ui.table_of_recording.setItem(row, 1, QTableWidgetItem(str(record.address)))
                self.ui.table_of_recording.setItem(row, 2, QTableWidgetItem(str(record.birthday)))
                self.ui.table_of_recording.setItem(row, 3, QTableWidgetItem(str(record.date_of_admission)))
                self.ui.table_of_recording.setItem(row, 4, QTableWidgetItem(str(record.fio_doctor)))
                self.ui.table_of_recording.setItem(row, 5, QTableWidgetItem(str(record.conclusion)))
        self.ui.tab_widget_work_state.setCurrentWidget(self.ui.tab_work_with_data)

    def __add_new_clinic_info(self, clinic_info) -> None:
        self.__clinic_info_service.create_patient(clinic_info)

    def __create_new_clinic_info(self)->None:
        dialog = AddingDataWindow()
        dialog.submitted.connect(self.__add_new_clinic_info)
        dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
