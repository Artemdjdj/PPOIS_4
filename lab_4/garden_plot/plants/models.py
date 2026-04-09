from django.db import models
from django.utils import timezone
from plot.models import PlotModel

from garden_plot.settings import TIME_OF_LAST_ADDING_WATER


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
    color = models.ForeignKey(ColorModel, on_delete=models.CASCADE, verbose_name="Цвет")
    diameter = models.PositiveIntegerField(verbose_name="Диаметер стебля")
    is_watered = models.BooleanField(default="False", verbose_name="Полито ли")
    time_of_last_adding_water = models.DateTimeField(auto_now_add=True, verbose_name="Дата последнего полива")
    image = models.ImageField(upload_to="plant_images", null=True, blank=True, verbose_name="Изображение")
    plot = models.ForeignKey(
        PlotModel,
        on_delete=models.CASCADE,
        related_name='plants',
        verbose_name="Садовый участок"
    )

    class Meta:
        db_table = "Plant"
        verbose_name = "Plant"
        verbose_name_plural = "Plants"

    @property
    def get_color(self):
        return self.color.name

    def update(self):
        current_time = timezone.now()
        if self.is_watered:
            if self.time_of_last_adding_water is not None and (
                    current_time - self.time_of_last_adding_water).seconds >= TIME_OF_LAST_ADDING_WATER:
                self.is_watered = False
                self.save()

    def update_time_of_last_adding_water(self):
        current_time = timezone.now()
        if self.time_of_last_adding_water is not None and (
                current_time - self.time_of_last_adding_water).seconds >= TIME_OF_LAST_ADDING_WATER:
            self.water(current_time)
        else:
            self.is_watered = False
            self.save()

    def water(self, my_time):
        self.is_watered = True
        self.time_of_last_adding_water = my_time
        self.save()
