from abc import ABC, abstractmethod
from src.utils.descriptor import NumberValidator
from src.main.settings import Color


class IPlant(ABC):
    height = NumberValidator()
    count_of_water = NumberValidator()

    def __init__(
        self,
        height: int | float,
        name: str,
        color: Color,
        count_of_water: int | float = None,
    ) -> None:
        self.height = height
        self.__name = name
        self.color = color
        self.count_of_water = count_of_water

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def color(self) -> str:
        return self.color.value

    @color.setter
    def color(self, color: Color) -> None:
        self.__color = color

    @abstractmethod
    def is_edible(self)->bool:
        pass


class Vegetable(IPlant):
    length_root = NumberValidator()

    def __init__(
        self,
        height: int | float,
        name: str,
        color: Color,
        length_root: int | float,
        count_of_water: int | float = None,
    ):
        super.__init__(height, name, color, count_of_water)
        self.length_root = length_root

    def get_type_of_plant(self):
        return "Vegetable"
    
    def is_edible(self)->bool:
        return True

class Fruit(IPlant):
    def __init__(
        self,
        height: int | float,
        name: str,
        color: Color,
        is_sweet: bool,
        count_of_water: int | float = None,
    ):
        super.__init__(height, name, color, count_of_water)
        self.__is_sweet = is_sweet

    @property
    def is_sweet(self) -> bool:
        return self.__is_sweet

    @is_sweet.setter
    def is_sweet(self, is_sweet: bool) -> None:
        self.__is_sweet = is_sweet

    def is_edible(self)->bool:
        return True


class DecorativePlant(IPlant):
    def __init__(
        self,
        height: int | float,
        name: str,
        color: Color,
        design: str,
        count_of_water: int | float = None,
    ):
        super.__init__(height, name, color, count_of_water)
        self.__design = design

    @property
    def design(self) -> str:
        return self.__design

    @design.setter
    def design(self, design: str) -> None:
        self.__design = design

    def is_edible(self)->bool:
        return False
