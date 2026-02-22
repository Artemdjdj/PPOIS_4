import re
from src.validator.basic_validator import BasicDateValidator
from src.exceptions.exceptions import DateError, BirthdayError, DateOfAdmissionError


class DateValidator(BasicDateValidator):
    def __init__(self, date: str) -> None:
        self.date = date

    def validate(self):
        pass


class BirthdayValidator(DateValidator):
    def validate(self):
        pattern = r"^\d{4}\-\d{2}\-\d{2}$"
        if not bool(re.match(pattern, self.date)):
            raise BirthdayError("Некорректный формат даты (2026-02-12)")


class DateOfAdmissionValidator(DateValidator):
    def validate(self):
        pattern = r"^\d{4}\-\d{2}\-\d{2}$"
        if not bool(re.match(pattern, self.date)):
            raise DateOfAdmissionError("Некорректный формат даты (2026-02-12)")
