from abc import ABC, abstractmethod

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from plot.models import PlotModel
from recreation_area.utils import BaseManager
from src.core.plot import Grill


class MeatTypeModel(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    slug = models.SlugField(max_length=30, verbose_name="URL")
    time_of_cooking = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(300)],
        verbose_name="Среднее время приготовления мин",
    )
    image = models.ImageField(
        upload_to="meat_images", null=True, blank=True, verbose_name="Изображение"
    )

    class Meta:
        db_table = "MeatType"
        verbose_name = "Тип мяса"
        verbose_name_plural = "Типы мяса"

    def __str__(self):
        return self.name


class RecreationAreaManager(BaseManager):
    def get_obj(self):
        try:
            return self.get()
        except RecreationAreaModel.DoesNotExist:
            return None


class RecreationAreaModel(models.Model):
    square = models.PositiveIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(10000)],
        verbose_name="Площадь",
    )
    perimeter = models.PositiveIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(10000)],
        verbose_name="Периметр",
    )
    is_clean = models.BooleanField(default=False, verbose_name="Убрана")
    plot = models.OneToOneField(
        PlotModel, on_delete=models.CASCADE, verbose_name="Участок"
    )
    objects = RecreationAreaManager()

    def save(self, *args, **kwargs):
        if not self.pk and RecreationAreaModel.objects.exists():
            raise ValidationError("Может существовать только одна зона отдыха.")
        super().save(*args, **kwargs)

    def get_fittings(self):
        return self.fittings.all()

    class Meta:
        db_table = "RecreationArea"
        verbose_name = "Зона отдыха"
        verbose_name_plural = "Зоны отдыха"

    def __str__(self):
        return f"Зона отдыха №{self.pk}"


class FittingModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(
        upload_to="recreation_area_images",
        null=True,
        blank=True,
        verbose_name="Изображение",
    )
    recreation_area = models.ForeignKey(
        RecreationAreaModel,
        on_delete=models.CASCADE,
        related_name="fittings",
        verbose_name="Зона отдыха",
    )

    class Meta:
        db_table = "Fitting"
        verbose_name = "Элемент декора"
        verbose_name_plural = "Элементы декора"

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
        RecreationAreaModel, on_delete=models.CASCADE, verbose_name="Зона отдыха"
    )
    objects = GrillManager()

    def save(self, *args, **kwargs):
        if not self.pk and GrillModel.objects.exists():
            raise ValidationError("Может существовать только один гриль.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Гриль {self.pk} для приготовления мясных блюд"

    def to_library_grill(self) -> Grill:
        return Grill()

    @classmethod
    def from_library_grill(
        cls, lib_grill: Grill, recreation_area: RecreationAreaModel
    ) -> "GrillModel":
        return cls(recreation_area=recreation_area)

    def update_from_library_grill(self, lib_grill: Grill) -> None:
        self.save()

    class Meta:
        db_table = "Grill"
        verbose_name = "Гриль"
        verbose_name_plural = "Грили"
