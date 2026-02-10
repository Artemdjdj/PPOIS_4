from src.utils.descriptor import NumberValidator


class Plot:
    width = NumberValidator()
    height = NumberValidator()

    def __init__(self, width: int | float, height: int | float) -> None:
        self.width = width
        self.height = height

    @property
    def square(self) -> int | float:
        return self.width * self.height

    @property
    def perimeter(self) -> int | float:
        return 2 * (self.width + self.height)
