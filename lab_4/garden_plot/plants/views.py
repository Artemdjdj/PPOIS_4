from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import PlantForm
from .models import PlantModel, ColorModel
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
    plot = PlotModel.objects.get_obj()
    colors = ColorModel.objects.all()
    if request.method == 'POST':
        form  = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.plot = plot
            plant.save()
            return HttpResponseRedirect(reverse('plants:index'))
    else:
        form = PlantForm()

    context = {
        'form': form,
        'colors': colors
    }

    return render(request, "plants/add_plant.html", context)