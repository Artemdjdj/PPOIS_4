from datetime import timedelta, datetime, timezone

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone as django_timezone

from plot.models import PlotModel
from recreation_area.utils import BaseManager

from garden_plot.exceptions import SystemIsNotActiveError, TooMuchPlantsAreWateredError
from garden_plot.settings import TIME_OF_LAST_ADDING_WATER
from garden_plot.exceptions import NoPlantsError

from src.core.irrigation_system import IrrigationSystem


class IrrigationSystemManager(BaseManager):
    def get_obj(self):
        try:
            return self.get()
        except IrrigationSystemModel.DoesNotExist:
            return None


def default_last_watering_time():
    return django_timezone.now() - timedelta(seconds=TIME_OF_LAST_ADDING_WATER + 1)


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

    def to_library_system(self):
        lib = IrrigationSystem()
        if self.is_active:
            lib.turn_on()
        else:
            lib.turn_of()
        lib.time_of_last_adding_water = self.time_of_last_adding_water.replace(tzinfo=None)
        return lib

    @classmethod
    def from_library_system(cls, lib, plot):
        dt = lib.time_of_last_adding_water
        if dt is not None:
            dt = dt.replace(tzinfo=timezone.utc)
        return cls(
            is_active=lib.is_active,
            time_of_last_adding_water=dt or django_timezone.now(),
            plot=plot,
        )

    def update_from_library_system(self, lib):
        self.is_active = lib.is_active
        dt = lib.time_of_last_adding_water
        if dt is not None:
            dt = dt.replace(tzinfo=timezone.utc)
        self.time_of_last_adding_water = dt or django_timezone.now()
        self.save()

    class Meta:
        db_table = 'IrrigationSystem'
        verbose_name = 'IrrigationSystem'
        verbose_name_plural = 'IrrigationSystems'