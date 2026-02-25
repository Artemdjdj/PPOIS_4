from datetime import date
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QIcon
from src.interface.ui.ui_adding_data_window import Ui_AddingDataWindow
from src.main.settings import MAIN_WINDOW_ICON
from src.validator.fio_validator import FioUserValidator, FioDoctorValidator
from src.validator.address_validator import BelarusAddressValidator
from src.exceptions.exceptions import (
    FioUserError,
    FioDoctorError,
    AddressError,
)


class AddingDataWindow(QDialog):
    submitted = Signal(str, str, date, date, str, str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_AddingDataWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(MAIN_WINDOW_ICON))
        self.setWindowTitle("Добавление новой записи")
        self.__add_functions()

    def __add_functions(self) -> None:
        self.ui.button_save.clicked.connect(lambda: self.__save_data())
        self.ui.button_clear.clicked.connect(lambda: self.__clear_data())
        self.ui.button_cancel.clicked.connect(self.reject)

    def __check_data(self) -> None:
        validator_fio_user = FioUserValidator(self.ui.line_edit_fio_user.text())
        validator_fio_user.validate()

        validator_address = BelarusAddressValidator(self.ui.line_edit_address.text())
        validator_address.validate()

        validator_fio_doctor = FioDoctorValidator(self.ui.line_edit_doctor.text())
        validator_fio_doctor.validate()

    def __save_data(self) -> None:
        try:
            self.__check_data()
            fio_user = self.ui.line_edit_fio_user.text()
            address = self.ui.line_edit_address.text()
            birthday = self.ui.calendarWidget.selectedDate().toPython()
            date_of_admission = self.ui.calendarWidget.selectedDate().toPython()
            fio_doctor = self.ui.line_edit_doctor.text()
            conclusion = self.ui.text_edit_doctor_promt.toPlainText()
            self.submitted.emit(
                fio_user, address, birthday, date_of_admission, fio_doctor, conclusion
            )
            self.accept()
        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка", f"{e}"
            )

    def __clear_data(self):
        self.ui.line_edit_fio_user.clear()
        self.ui.line_edit_address.clear()
        self.ui.line_edit_doctor.clear()
        self.ui.text_edit_doctor_promt.clear()
