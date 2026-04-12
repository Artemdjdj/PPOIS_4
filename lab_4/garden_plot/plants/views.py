from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import PlantForm
from .models import PlantModel, ColorModel
from plot.models import PlotModel
from src.core.plant import Plant, Color


def index(request):
    plants = PlantModel.objects.all()
    for plant in plants:
        convert_plant = plant.to_library_plant()
        convert_plant.update()
        plant = plant.update_from_library_plant(convert_plant)
    plot = PlotModel.objects.get_obj()
    page_number = request.GET.get("page")

    paginator = Paginator(plants, 4)
    page_obj = paginator.get_page(page_number)
    context = {"plants": plants, "page_obj": page_obj, "plot": plot}
    return render(request, "plants/index.html", context)


def add_plant(request):
    plot = PlotModel.objects.get_obj()
    colors = ColorModel.objects.all()
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.plot = plot
            plant.save()
            return HttpResponseRedirect(reverse("plants:index"))
    else:
        form = PlantForm()

    context = {"plot": plot, "form": form, "colors": colors}

    return render(request, "plants/add_plant.html", context)


def delete_plant(request, plant_id):
    plant = get_object_or_404(PlantModel, id=plant_id)
    plant.delete()
    return HttpResponseRedirect(reverse("plants:index"))


def water_plant(request, plant_id):
    plant = get_object_or_404(PlantModel, id=plant_id)
    convert_plant = plant.to_library_plant()
    convert_plant.update_time_of_last_adding_water()
    plant.update_from_library_plant(convert_plant)
    return HttpResponseRedirect(reverse("plants:index"))
