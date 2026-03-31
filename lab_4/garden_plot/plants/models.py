from django.db import models
from plot.models import PlotModel

class ColorModel(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название")
    slug = models.SlugField(max_length=40, verbose_name="URL")

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
    time_of_last_adding_water = models.PositiveIntegerField(verbose_name="Время с последнего полива в часах")
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
