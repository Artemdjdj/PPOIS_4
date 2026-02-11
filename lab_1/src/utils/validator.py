from abc import ABC, abstractmethod
from src.exceptions.exceptions import PositionError, NoneObjectError
from src.core.plot import RecreationArea


class IValidator(ABC):
    @abstractmethod
    def validate(self) -> None:
        pass


class PositionValidator(IValidator):
    def __init__(self, len_of_arr: int, position: int) -> None:
        self.__len_of_arr = len_of_arr
        self.__position = position

    def validate(self):
        if not isinstance(self.__position, int):
            raise TypeError("Некорректный формат позиции в списке")
        if abs(self.__position) >= self.__len_of_arr:
            raise PositionError("Некорректая позиция")