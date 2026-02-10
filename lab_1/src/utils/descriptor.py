from typing import Any


class NumberValidator:
    def __init__(
        self, max_value: int | float = None
    ) -> None:
        self.min_value = 0
        self.max_value = max_value

    def __set_name__(self, owner: Any, name: str) -> None:
        self.name = f"__{name}"

    def __get__(self, instance: Any, owner: Any) -> int | float:
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance: Any, value: int | float) -> None:
        if not isinstance(value, (int|float)):
            raise TypeError("The value is not int and not float")
        elif value <= self.min_value:
            raise ValueError(f"The value is too small, min value  is {self.min_value}")
        elif self.max_value is not None and value > self.max_value:
            raise ValueError(f"The value is too big, max value  is {self.max_value}")
        instance.__dict__[self.name] = value