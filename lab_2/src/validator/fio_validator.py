import re
from src.validator.basic_validator import BasicValidator
from src.exceptions.exceptions import FioUserError, FioDoctorError


class FioValidator(BasicValidator):
    def __init__(self, name: str) -> None:
        self._name = name

    def validate(self):
        pass


class FioUserValidator(FioValidator):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def validate(self):
        pattern = r"^([А-ЯЁ][а-яё]+\s){2}[А-ЯЁ][а-яё]+$"
        if not bool(re.match(pattern, self._name)):
            raise FioUserError("Некоректно введено имя(фамилия, отчество)")


class FioDoctorValidator(FioValidator):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def validate(self):
        pattern = r"^([А-ЯЁ][а-яё]+\s){2}[А-ЯЁ][а-яё]+$"
        if not bool(re.match(pattern, self._name)):
            raise FioDoctorError("Некоректно введено имя(фамилия, отчество)")
