from django.shortcuts import render

from .models import PlantModel
from plot.models import PlotModel


def index(request):
    plants = PlantModel.objects.all()
    plot = PlotModel.objects.get_obj()
    context = {
        'plants':plants,
        'plot':plot
    }
    return render(request, 'plants/index.html', context)

def add_plant(request):
    return render(request, "plants/add_plant.html")