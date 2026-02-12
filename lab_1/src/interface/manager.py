import json
from abc import ABC, abstractmethod
from typing import Dict
from src.core.plot import GardenPlot


class BasicDataManager(ABC):
    @abstractmethod
    def save_garden(self) -> None:
        pass

    @abstractmethod
    def load_garden(self) -> GardenPlot:
        pass


class JsonDataManager(BasicDataManager):
    def __init__(self, filename: str):
        self._filename = filename

    def save_to_json(self, data: Dict) -> None:
        try:
            with open(self._filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Error saving file {self._filename}: {e}")

    def load_from_json(self) -> Dict:
        try:
            with open(self._filename, "r", encoding="utf-8") as f:
                content = f.read()
                if not content:
                    return {}
                return json.loads(content)
        except IOError as e:
            raise IOError(f"Ошибка загрузки из файла {self._filename}: {e}")


class GardenJsonDataManager(JsonDataManager):
    def __init__(self, garden_plot: GardenPlot, filename: str) -> None:
        super().__init__(filename)
        self.__garden_plot = garden_plot

    def save_garden(self) -> None:
        self.save_to_json(self.__garden_plot.create_dict())

    def load_garden(self) -> GardenPlot:
        data = self.load_from_json()
        if not data:
            raise ValueError("В данный момент сохраненного садового участка нет")
        return GardenPlot.create_object_from_dict(data)
