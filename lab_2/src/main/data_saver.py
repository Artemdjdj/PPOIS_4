from datetime import date

from PySide6.QtWidgets import QLineEdit
from src.main.utils import DateConverter


class DataSaver:
    def __init__(
        self,
        fio_user: QLineEdit,
        address: QLineEdit,
        birthday: QLineEdit,
        date_of_admission: QLineEdit,
        fio_doctor: QLineEdit,
    ) -> None:
        self.fio_user = fio_user
        self.address = address
        self.birthday = birthday
        self.date_of_admission = date_of_admission
        self.fio_doctor = fio_doctor

    def save_data(self) -> tuple[str, str, date | None, date | None, str]:
        birthday_text = self.birthday.text()
        try:
            birthday = DateConverter.to_date(self.birthday.text())
        except BaseException:
            birthday = birthday_text

        date_of_admission_text = self.date_of_admission.text()
        try:
            date_of_admission = DateConverter.to_date(self.date_of_admission.text())

        except BaseException:
            date_of_admission = date_of_admission_text
        return (
            self.fio_user.text(),
            self.address.text(),
            birthday,
            date_of_admission,
            self.fio_doctor.text(),
        )
