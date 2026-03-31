from django.shortcuts import render

from irrigation_system.models import IrrigationSystemModel

from plot.models import PlotModel


def index(request):
    irrigation_system = IrrigationSystemModel.objects.get_obj()
    if irrigation_system is None:
        plot = PlotModel.objects.get_obj()
        if plot is not None:
            irrigation_system = IrrigationSystemModel.objects.create(plot=plot)
        else:
            return render(request, "main/plot_is_not_created.html")
    context = {
        "irrigation_system": irrigation_system,
    }
    return render(request, "irrigation_system/index.html", context)

def activate(request):
    return render(request, "irrigation_system/activate.html")

def deactivate(request):
    return render(request, "irrigation_system/deactivate.html")