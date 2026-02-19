import re
from src.validator.basic_validator import BasicAddressValidator
from src.exceptions.exceptions import AddressError


class BelarusAddressValidator(BasicAddressValidator):
    def __init__(self, address: str) -> None:
        self.__address = address

    def validate(self):
        pattern = r"^г\.\s*[А-Яа-яЁё]+\s*,\s*ул\.\s*[А-Яа-яЁё]+\s*,\s*д\.\s*\d+[a-z]?$"
        if not bool(re.match(pattern, self.__address)):
            raise AddressError(
                "Некорректный форат адреса(г. Название, ул. Название, д. Номер(корпус если есть а,б,...я))"
            )
