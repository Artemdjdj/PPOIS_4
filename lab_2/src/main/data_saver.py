from datetime import date

from PySide6.QtWidgets import QTableWidget, QTabWidget, QTableWidgetItem, QLineEdit
from src.db.models.clinic import ClinicInfoBase
from src.main.utils import DateConverter


class DataSaver:
    def __init__(self, fio_user: QLineEdit, address: QLineEdit, birthday: QLineEdit, date_of_admission: QLineEdit,
                 fio_doctor: QLineEdit)->None:
        self.fio_user = fio_user
        self.address = address
        self.birthday = birthday
        self.date_of_admission = date_of_admission
        self.fio_doctor = fio_doctor

    def save_data(self) -> tuple[str, str, date | None, date | None, str]:
        birthday = self.birthday.text()
        birthday = DateConverter.to_date(self.birthday.text()) if birthday else None
        date_of_admission = self.date_of_admission.text()
        date_of_admission = DateConverter.to_date(
            self.date_of_admission.text()) if date_of_admission else None
        return self.fio_user.text(), self.address.text(), birthday, date_of_admission, self.fio_doctor.text()
