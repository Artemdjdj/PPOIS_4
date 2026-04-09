import time

from django.shortcuts import render
from django.utils import timezone

from irrigation_system.models import IrrigationSystemModel
from plot.models import PlotModel

from garden_plot.settings import TIME_OF_LAST_ADDING_WATER

from plants.models import PlantModel


def index(request):
    irrigation_system = IrrigationSystemModel.objects.get_obj()
    plot = PlotModel.objects.get_obj()
    result = None

    if irrigation_system is None:
        if plot is not None:
            irrigation_system = IrrigationSystemModel.objects.create(plot=plot)

    if irrigation_system is not None:
        plants = PlantModel.objects.all()
        try:
            irrigation_system.is_active = True
            irrigation_system.save()
            result = irrigation_system.water(plants)
        except Exception as e:
            result = e.msg
            irrigation_system.is_active = False
            irrigation_system.save()

    context = {
        "irrigation_system": irrigation_system,
        "plot": plot,
        'result': result
    }

    return render(request, "irrigation_system/index.html", context)
