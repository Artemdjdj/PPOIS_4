from django.shortcuts import render

from plot.models import PlotModel


def index(request):
    plot = PlotModel.objects.get_obj()

    context = {"plot": plot}
    return render(request, "main/index.html", context)
