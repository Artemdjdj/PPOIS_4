from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import FittingForm
from .models import FittingModel, GrillModel, MeatTypeModel, RecreationAreaModel
from plot.models import PlotModel
from plot.forms import RecreationAreaForm


def index(request):
    fittings = FittingModel.objects.all()
    plot = PlotModel.objects.get_obj()
    recreation_area = RecreationAreaModel.objects.get_obj()

    context = {
        'plot':plot,
        'recreation_area':recreation_area,
        'fittings': fittings
    }

    return render(request, 'recreation_area/index.html', context)

def recreation_area_info(request):
    recreation_area = RecreationAreaModel.objects.get_obj()

    context = {
        'recreation_area':recreation_area,
        'decor_count': len(recreation_area.get_fittings()) if recreation_area else None
    }
    return render(request, "recreation_area/recreation_area_info.html", context)

def add_recreation_area(request):
    plot = PlotModel.objects.get_obj()
    if request.method == "POST":
        form = RecreationAreaForm(data=request.POST, plot=plot)
        if form.is_valid():
            recreation_area = form.save(commit=False)
            recreation_area.plot = plot
            recreation_area.save()
            return redirect('recreation_area:index')
    else:
        form = RecreationAreaForm(plot=plot)

    context = {
        'form': form,
        'plot':plot
    }
    return render(request, "recreation_area/add_recreation_area.html", context)

def delete_recreation_area(request):
    if request.method == "POST":
        RecreationAreaModel.objects.delete_obj()
        return HttpResponseRedirect(reverse('recreation_area:index'))
    return render(request, "recreation_area/index.html")

def grill(request):
    grill_res = GrillModel.objects.get_obj()

    meat_types =MeatTypeModel.objects.all()
    meat_type_last = None
    result_time_of_frying = None
    if request.method == 'POST':
        meat_id = request.POST.get('meat_type')
        meat_type_last = MeatTypeModel.objects.get(id=meat_id)
        result_time_of_frying = grill_res.fry(meat_type_last)

    context = {
        'grill': grill_res,
        'meat_types': meat_types,
        'result_time_of_frying': result_time_of_frying,
        'meat_type_last': meat_type_last,
    }
    return render(request, 'recreation_area/grill.html', context)

def create_grill(request):
    if request.method == 'POST':
        GrillModel.objects.create()
        return HttpResponseRedirect(reverse('recreation_area:grill'))
    return render(request, "recreation_area/grill.html")


def delete_grill(request):
    if request.method == "POST":
        GrillModel.objects.delete_obj()
        return HttpResponseRedirect(reverse('recreation_area:grill'))
    return render(request, "recreation_area/grill.html")


def add_fitting(request):
    recreation_area = RecreationAreaModel.objects.get_obj()
    if request.method == "POST":
        form  = FittingForm(data= request.POST, files=request.FILES)
        if form.is_valid():
            fitting = form.save(commit=False)
            fitting.recreation_area = recreation_area
            fitting.save()
            return HttpResponseRedirect(reverse('recreation_area:index'))
    else:
        form = FittingForm()

    context = {
        'form': form,
    }
    return render(request, 'recreation_area/add_fitting.html', context)


def delete_fitting(request, fitting_id):
    fitting = get_object_or_404(FittingModel, id=fitting_id)
    fitting.delete()
    return HttpResponseRedirect(reverse("recreation_area:index"))