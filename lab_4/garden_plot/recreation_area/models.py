from abc import ABC, abstractmethod

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from plot.models import PlotModel
from recreation_area.utils import BaseManager



class MeatTypeModel(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    slug = models.SlugField(max_length=30, verbose_name="URL")
    time_of_cooking = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(300)],
                                         verbose_name="Среднее время приготовления мин")

    class Meta:
        db_table = 'MeatType'
        verbose_name = 'MeatType'
        verbose_name_plural = 'MeatTypes'

    def __str__(self):
        return self.name

class RecreationAreaManager(BaseManager):
    def get_obj(self):
        try:
            return self.get()
        except RecreationAreaModel.DoesNotExist:
            return None

class RecreationAreaModel(models.Model):
    square = models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(10000)],
                                         verbose_name="Площадь")
    perimeter = models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(10000)],
                                            verbose_name="Периметр")
    is_clean = models.BooleanField(default=False, verbose_name="Убрана")
    plot = models.OneToOneField(
        PlotModel,
        on_delete=models.CASCADE,
        verbose_name="Участок"
    )

    objects = RecreationAreaManager()

    def save(self, *args, **kwargs):
        if not self.pk and RecreationAreaModel.objects.exists():
            raise ValidationError("Может существовать только одна зона отдыха.")
        super().save(*args, **kwargs)

    def get_fittings(self):
        return self.fittings.all()

    class Meta:
        db_table = 'RecreationArea'
        verbose_name = 'RecreationArea'
        verbose_name_plural = 'RecreationAreas'

    def __str__(self):
        return f"Зона отдыха №{self.pk}"


class FittingModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to="recreation_area_images", null=True, blank=True, verbose_name="Изображение")
    recreation_area = models.ForeignKey(
        RecreationAreaModel,
        on_delete=models.CASCADE,
        related_name='fittings',
        verbose_name="Зона отдыха"
    )
    class Meta:
        db_table = 'Fitting'
        verbose_name = 'Fitting'
        verbose_name_plural = 'Fittings'

    def __str__(self):
        return self.name

class GrillManager(BaseManager):
    def get_obj(self):
        try:
            return self.get()
        except GrillModel.DoesNotExist:
            return None

class GrillModel(models.Model):
    recreation_area = models.ForeignKey(
        RecreationAreaModel,
        on_delete=models.CASCADE,
        verbose_name="Зона отдыха"
    )
    objects = GrillManager()

    def save(self, *args, **kwargs):
        if not self.pk and GrillModel.objects.exists():
            raise ValidationError("Может существовать только один гриль.")
        super().save(*args, **kwargs)


    def fry(self, meat) -> str:
        return f"мясо приготовилось за {meat.time_of_cooking} минут"

    def __str__(self):
        return f"Гриль {self.pk} для приготовления мясных блюд"

    class Meta:
        db_table = 'Grill'
        verbose_name = 'Grill'
        verbose_name_plural = 'Grills'





