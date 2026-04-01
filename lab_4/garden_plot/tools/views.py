from django.shortcuts import render

from .models import ToolModel
from plot.models import PlotModel


def index(request):
    tools = ToolModel.objects.all()
    plot = PlotModel.objects.get_obj()
    context = {
        'tools': tools,
        'plot':plot,
    }
    return render(request, "tools/index.html", context)


def add_tool(request):
    return render(request, "tools/add_tool.html")