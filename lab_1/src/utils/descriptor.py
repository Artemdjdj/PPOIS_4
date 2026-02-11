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
            raise TypeError("Число должно быть int либо float!")
        elif value <= self.min_value:
            raise ValueError(f"Число меньше минимального, минимальное: {self.min_value}")
        elif self.max_value is not None and value > self.max_value:
            raise ValueError(f"Число больше максимального, максимальное: {self.max_value}")
        instance.__dict__[self.name] = value


class IntegerValidator:
    def __init__(
        self, min_value :int = None,max_value: int = None
    ) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, name):
        self.name = f"__{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Число должно быть целым!")
        elif value < 0:
            raise ValueError("Число не может быть отрицательным")
        elif value <= self.min_value:
            raise ValueError(f"Число меньше минимального, минимальное: {self.min_value}")
        elif self.max_value is not None and value > self.max_value:
            raise ValueError(f"Число больше максимального, максимальное: {self.max_value}")
        instance.__dict__[self.name] = value
