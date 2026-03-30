from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import PlotForm
from .models import PlotModel, SoilModel


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
        PlotModel.objects.delete_obj()
        return HttpResponseRedirect(reverse('plot:plot_info'))
    return render(request, "plot/plot_info.html")
