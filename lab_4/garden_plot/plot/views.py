from decimal import Decimal

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PlotForm
from .models import PlotModel, SoilModel
from garden_plot.exceptions import BigAmountOfFertilizerError


def add_plot(request):
    soil_types = SoilModel.objects.all()
    if request.method == "POST":
        form = PlotForm(data=request.POST)
        if form.is_valid():
            plot = form.save(commit=False)
            plot.save()
            return HttpResponseRedirect(reverse('plot:plot_info'))
    else:
        form = PlotForm()
    context = {
        'form': form,
        'soil_types': soil_types
    }
    return render(request, "plot/add_plot.html", context)

def plot_info(request):
    plot = PlotModel.objects.get_obj()

    context = {
        'plot': plot,
        'tools_count':len(plot.get_tools()) if plot else None,
        'plants_count':len(plot.get_plants()) if plot else None,
    }
    return render(request, "plot/plot_info.html", context)

def delete_plot(request):
    if request.method == "POST":
        plot = PlotModel.objects.get_obj()
        soil = plot.soil
        soil.clear_soil()
        PlotModel.objects.delete_obj()
        return HttpResponseRedirect(reverse('plot:plot_info'))
    return render(request, "plot/plot_info.html")


def soil_info(request):
    plot = PlotModel.objects.get_obj()
    if plot is None:
        context = {'plot': None}
        return render(request, "plot/soil.html", context)

    coeff = request.GET.get('coeff')
    if coeff and coeff != "":
        try:
            coeff = Decimal(coeff)
            soil = plot.soil
            soil.fertilize(coeff)
        except Exception:
            return redirect('plot:soil_info')

    context = {
        'plot': plot,
        'result': plot.soil.coeff_fertilizer,
    }
    return render(request, "plot/soil.html", context)