import re
from basic_validator import BasicValidator
from src.exceptions.exceptions import FioError


class FioValidator(BasicValidator):
    def __init__(self, name: str) -> None:
        self.__name = name

    def validate(self):
        pattern = r"^[А-ЯЁ][а-яё]*$"
        if not bool(re.match(pattern, self.__name)):
            raise FioError("Некоректно введено имя(фамилия, отчество)")
