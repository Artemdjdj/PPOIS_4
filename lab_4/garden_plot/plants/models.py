from django.db import models
from django.utils import timezone
from plot.models import PlotModel
import time
from datetime import datetime
from garden_plot.settings import TIME_OF_LAST_ADDING_WATER
from src.core.plant import Plant, Color


class ColorModel(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=40, unique=True, verbose_name="URL")

    class Meta:
        db_table = "Color"
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return self.name

class PlantModel(models.Model):
    height = models.PositiveIntegerField(verbose_name="Высота")
    name = models.CharField(max_length=50, verbose_name="Имя")
    color = models.ForeignKey(
        "ColorModel", on_delete=models.CASCADE, verbose_name="Цвет"
    )
    diameter = models.PositiveIntegerField(verbose_name="Диаметер стебля")
    is_watered = models.BooleanField(default=False, verbose_name="Полито ли")
    time_of_last_adding_water = models.DateTimeField(
        null=True,
        blank=True,
        default=timezone.now,
        verbose_name="Дата последнего полива",
    )
    image = models.ImageField(
        upload_to="plant_images", null=True, blank=True, verbose_name="Изображение"
    )
    plot = models.ForeignKey(
        PlotModel,
        on_delete=models.CASCADE,
        related_name="plants",
        verbose_name="Садовый участок",
    )

    class Meta:
        db_table = "Plant"
        verbose_name = "Plant"
        verbose_name_plural = "Plants"

    @property
    def get_color(self):
        return self.color.name

    def to_library_plant(self) -> Plant:
        lib_color = Color()
        lib_color.color = self.color.name
        plant = Plant(
            height=self.height,
            name=self.name,
            color=lib_color,
            is_watered=self.is_watered,
            diameter=self.diameter,
        )
        plant.time_of_last_adding_water = self.time_of_last_adding_water
        return plant

    @classmethod
    def from_library_plant(cls, plant: Plant, plot: PlotModel, image=None):
        color_obj, _ = ColorModel.objects.get_or_create(name=plant.color)
        return cls(
            height=plant.height,
            name=plant.name,
            color=color_obj,
            diameter=plant.diameter,
            is_watered=plant.is_watered,
            time_of_last_adding_water=plant.time_of_last_adding_water,
            plot=plot,
            image=image,
        )

    def update_from_library_plant(self, plant: Plant) -> None:
        color_obj, _ = ColorModel.objects.get_or_create(name=plant.color)
        self.color = color_obj
        self.height = plant.height
        self.name = plant.name
        self.diameter = plant.diameter
        self.is_watered = plant.is_watered
        self.time_of_last_adding_water = plant.time_of_last_adding_water
        self.save()

    def water(self, my_time=None):
        if my_time is None:
            my_time = timezone.now()
        lib_plant = self.to_library_plant()
        lib_plant.water(my_time)
        self.update_from_library_plant(lib_plant)
