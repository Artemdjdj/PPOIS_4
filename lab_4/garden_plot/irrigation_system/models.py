from datetime import timedelta

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from plot.models import PlotModel
from recreation_area.utils import BaseManager

from garden_plot.exceptions import SystemIsNotActiveError, TooMuchPlantsAreWateredError

from garden_plot.settings import TIME_OF_LAST_ADDING_WATER

from garden_plot.exceptions import NoPlantsError


class IrrigationSystemManager(BaseManager):
    def get_obj(self):
        try:
            return self.get()
        except IrrigationSystemModel.DoesNotExist:
            return None

def default_last_watering_time():
    return timezone.now() - timedelta(seconds=TIME_OF_LAST_ADDING_WATER + 1)

class IrrigationSystemModel(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Включена ли')
    time_of_last_adding_water = models.DateTimeField(
        default=default_last_watering_time,
        verbose_name="Дата последнего полива"
    )
    plot = models.OneToOneField(
        PlotModel,
        on_delete=models.CASCADE,
        verbose_name="Участок"
    )
    objects = IrrigationSystemManager()

    def save(self, *args, **kwargs):
        if not self.pk and IrrigationSystemModel.objects.exists():
            raise ValidationError("Может существовать только одна система полива.")
        super().save(*args, **kwargs)

    def water(self, plants) -> str:
        if not self.is_active:
            raise SystemIsNotActiveError("Система автоматического полива не включена")

        if len(plants) == 0:
            raise NoPlantsError("У вас нет растений, прежде чем включить полив, добавьте растения на садовый участок")

        if not self.time_of_last_adding_water or (timezone.now() - self.time_of_last_adding_water).total_seconds() >= TIME_OF_LAST_ADDING_WATER:
            for plant in plants:
                plant.update_time_of_last_adding_water()
            self.is_active = False
            self.time_of_last_adding_water = timezone.now()
            self.save()

        else:
            raise TooMuchPlantsAreWateredError("Растения недавно были политы, нужно, чтобы прошло время (10 секунд минимум)")

        return f"Не политые растения были успешно политы, вскоре вы нужно будет их снова полить"

    class Meta:
        db_table = 'IrrigationSystem'
        verbose_name = 'IrrigationSystem'
        verbose_name_plural = 'IrrigationSystems'