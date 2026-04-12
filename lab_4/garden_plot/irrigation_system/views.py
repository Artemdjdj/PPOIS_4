import time

from django.shortcuts import render
from django.utils import timezone

from irrigation_system.models import IrrigationSystemModel
from plot.models import PlotModel
from plants.models import PlantModel


def index(request):
    irrigation_system = IrrigationSystemModel.objects.get_obj()
    plot = PlotModel.objects.get_obj()
    result = None

    if irrigation_system is None:
        if plot is not None:
            irrigation_system = IrrigationSystemModel.objects.create(plot=plot)

    if irrigation_system is not None:
        plant_models = PlantModel.objects.all()
        new_plants = [p.to_library_plant() for p in plant_models]
        try:
            irrigation_system.is_active = True
            irrigation_system.save()
            convert_irrigation_system = irrigation_system.to_library_system()
            print(f"количество {len(new_plants)}")
            result = convert_irrigation_system.water(new_plants)
            irrigation_system.update_from_library_system(convert_irrigation_system)
            for i in range(len(plant_models)):
                plant_models[i].update_from_library_plant(new_plants[i])
        except Exception as e:
            result = str(e)
            irrigation_system.is_active = False
            irrigation_system.save()

    context = {"irrigation_system": irrigation_system, "plot": plot, "result": result}

    return render(request, "irrigation_system/index.html", context)
