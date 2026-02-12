import pytest
from src.exceptions.exceptions import ColorError
from src.core.plant import Color, Plant


class TestColor:
    def test_color_correct(self):
        color = Color()
        color.color = "красный"
        assert color.color == "красный"

    def test_color_incorrect(self):
        color = Color()
        with pytest.raises(ColorError):
            color.color = "серо-буро-малиновый"

    def test_color_up(self):
        color = Color()
        color.color = "КРАСНЫЙ"
        assert color.color == "красный"


class TestPlant:
    def test_plant_getters(self):
        color = Color()
        color.color = "желтый"
        plant = Plant(height=20.5, name="Бархатцы", color=color, diameter=8)
        assert plant.height == 20.5
        assert plant.name == "Бархатцы"
        assert plant.color == "желтый"
        assert not plant.is_watered
        assert plant.diameter == 8

    def test_plant_initial_watered(self):
        color = Color()
        color.color = "белый"
        plant = Plant(30, "Ромашка", color, is_watered=True, diameter=10)
        assert plant.is_watered

    def test_set_is_watered(self):
        plant = Plant(10, "Кактус", Color(), diameter=5)
        plant.is_watered = True
        assert plant.is_watered

    def test_plant_str(self):
        color = Color()
        color.color = "зеленый"
        plant = Plant(100, "папоротник", color, diameter=100)
        assert str(plant) == "Растение папоротник высота которого: 100"

    def test_invalid_height(self):
        color = Color()
        with pytest.raises(ValueError):
            Plant(-5, "Василек", color, diameter=1)

    def test_invalid_diameter(self):
        color = Color()
        color.color = "зеленый"
        with pytest.raises(ValueError):
            Plant(10, "огромный баобаб", color, diameter=1000000000)
