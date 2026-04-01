from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import ToolForm
from .models import ToolModel, ToolTypeModel, ToolStateModel
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
    tool_types = ToolTypeModel.objects.all()
    plot = PlotModel.objects.get_obj()
    if request.method == "POST":
        tool_form = ToolForm(data= request.POST, files=request.FILES)
        if tool_form.is_valid():
            tool = tool_form.save(commit=False)
            tool_state = ToolStateModel.objects.get(name="идеальное")
            tool.usage_count = 0
            tool.state = tool_state
            tool.plot = plot
            tool.save()
            return HttpResponseRedirect(reverse("tools:index"))
    else:
        tool_form = ToolForm()

    context = {
        'tool_types': tool_types,
        'form': tool_form,
    }
    return render(request, "tools/add_tool.html", context)


def delete_tool(request, tool_id):
    tool = get_object_or_404(ToolModel, id=tool_id)
    tool.delete()
    return HttpResponseRedirect(reverse("tools:index"))