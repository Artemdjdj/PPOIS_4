import pytest
from src.core.plot import RecreationArea, Grill, GardenPlot
from src.core.plant import Color, Plant
from src.core.soil import SoilType
from src.core.tool import Tool
from src.exceptions.exceptions import (
    GrillDoesNotExist,
    PositionError,
    BigAmountOfFertilizerError,
    SizeError,
)


class TestRecreationArea:
    def test_initial_area(self):
        area = RecreationArea(56, 67)
        assert area.square == 56
        assert area.perimeter == 67
        assert area.get_decorative_fittings() == set()
        assert area.is_clean

    def test_add_base_manipulation_with_decor_elems(self):
        area = RecreationArea(20, 15)
        area.add_decorative_fitting("качели")
        area.add_decorative_fitting("скамейка")
        assert "качели" in area.get_decorative_fittings()
        assert len(area.get_decorative_fittings()) == 2
        area.remove_decorative_fitting("качели")
        assert len(area.get_decorative_fittings()) == 1

    def test_put_remove_grill(self):
        area = RecreationArea(30, 20)
        assert area.put_grill()
        assert not area.put_grill()
        assert not area.is_clean
        assert area.remove_grill()
        assert not area.remove_grill()

    def test_use_grill_without_grill(self):
        area = RecreationArea(10, 10)
        with pytest.raises(GrillDoesNotExist):
            area.use_grill()

    def test_clean_area(self):
        area = RecreationArea(40, 35)
        area.put_grill()
        assert not area.is_clean
        area.clean()
        assert area.is_clean
        area.clean()
        assert area.is_clean


class TestGardenPlot:
    def test_initial_plot(self):
        plot = GardenPlot(100, 50, SoilType.LOAMY, 200)
        assert plot.square == 100
        assert plot.perimeter == 50
        assert plot.plants == []
        assert plot.tools == []
        assert plot.recreation_area is None

    def test_plant_and_remove_plant(self):
        plot = GardenPlot(101, 54, SoilType.SANDY, 200)
        color = Color()
        color.color = "красный"
        plant = Plant(30, "Роза", color, diameter=10)
        plot.plant_plant(plant)
        assert len(plot.plants) == 1
        assert plot.plants[0].name == "Роза"
        plot.remove_plant(0)
        assert len(plot.plants) == 0

    def test_remove_plant_invalid_position(self):
        plot = GardenPlot(100, 50, SoilType.CLAY, 200)
        with pytest.raises(PositionError):
            plot.remove_plant(5)

    def test_remove_plant_invalid_negative_position(self):
        plot = GardenPlot(104, 54, SoilType.CLAY, 200)
        with pytest.raises(PositionError):
            plot.remove_plant(-5)

    def test_clear_all_plants(self):
        plot = GardenPlot(100, 50, SoilType.PEATY, 200)
        color = Color()
        color.color = "желтый"
        plot.plant_plant(Plant(10, "Одуванчик", color, diameter=5))
        plot.plant_plant(Plant(15, "Лютик", color, diameter=6))
        assert len(plot.plants) == 2
        plot.clear_garden_of_all_plants()
        assert len(plot.plants) == 0

    def test_water_plants(self):
        plot = GardenPlot(100, 50, SoilType.CHERNOZEM, 50)
        color = Color()
        color.color = "зеленый"
        plant1 = Plant(20, "Папоротник", color, diameter=4)
        plant2 = Plant(25, "Колокольчик", color, diameter=5)
        plot.plant_plant(plant1)
        plot.plant_plant(plant2)
        plot.water_plants(30)
        assert plant1.is_watered is True
        assert plant2.is_watered is True

    def test_fertilize_soil(self):
        plot = GardenPlot(100, 50, SoilType.LOAMY, 200)
        with pytest.raises(BigAmountOfFertilizerError):
            plot.fertilize_soil(3)

    def test_create_recreation_area(self):
        plot = GardenPlot(200, 150, SoilType.CLAY, 300)
        area = RecreationArea(50, 40)
        plot.create_recreation_area(area)
        assert plot.recreation_area is area
        big_area = RecreationArea(250, 200)
        with pytest.raises(SizeError):
            plot.create_recreation_area(big_area)

    def test_tools_operations(self):
        plot = GardenPlot(100, 50, SoilType.SANDY, 100)
        tool1 = Tool("Грабли", "Gardena", "Веерные грабли")
        tool2 = Tool("Секатор", "Fiskars", "Садовый секатор")
        plot.add_tool(tool1)
        plot.add_tool(tool2)
        assert len(plot.tools) == 2
        plot.remove_tool(0)
        assert len(plot.tools) == 1
        assert plot.tools[0].name == "Секатор"
        plot.clear_garden_of_all_tools()
        assert plot.tools == []
        with pytest.raises(PositionError):
            plot.remove_tool(0)

    def test_tool_maintenance(self):
        plot = GardenPlot(100, 50, SoilType.LOAMY, 100)
        tool = Tool("Топор", "Husqvarna", "Обычный")
        plot.add_tool(tool)
        tool.perform_task(15)
        assert (
            plot.tool_maintenance(0)
            == "Инструмент имел небольшие дефекты, теперь все готово инструмент и хорошем состоянии"
        )
        assert tool.state == "хорошее"
