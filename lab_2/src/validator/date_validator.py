import re
from basic_validator import BasicDateValidator
from src.exceptions.exceptions import DateError


class DateValidator(BasicDateValidator):
    def __init__(self, date: str) -> None:
        self.__date = date

    def validate(self):
        pattern = r"^\d{4}\.\d{2}\.\d{2}$"
        if not bool(re.match(pattern, self.__date)):
            raise DateError("Некорректный формат даты (2026.02.12)")
