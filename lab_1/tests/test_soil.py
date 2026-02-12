import pytest
from src.core.soil import Soil, SoilType
from src.exceptions.exceptions import BigAmountOfFertilizerError


class TestSoil:
    def test_soil_creation(self):
        soil = Soil(SoilType.CHERNOZEM)
        assert soil.type_of_soil == "чернозём"

    def test_set_soil_type(self):
        soil = Soil()
        soil.type_of_soil = "песчаная"
        assert soil.type_of_soil == "песчаная"

    def test_fertilize_success(self):
        soil = Soil()
        with pytest.raises(BigAmountOfFertilizerError):
            soil.fertilize(1)

    def test_fertilize_too_much(self):
        soil = Soil()
        with pytest.raises(BigAmountOfFertilizerError):
            soil.fertilize(2)
