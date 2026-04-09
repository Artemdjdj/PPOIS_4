from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import ToolForm
from .models import ToolModel, ToolTypeModel, ToolStateModel
from plot.models import PlotModel


def index(request):
    tools = ToolModel.objects.all()
    plot = PlotModel.objects.get_obj()
    page_number = request.GET.get("page")

    paginator = Paginator(tools, 4)
    page_obj = paginator.get_page(page_number)
    context = {
        'tools': tools,
        'plot': plot,
        'page_obj': page_obj,
    }
    return render(request, "tools/index.html", context)


def add_tool(request):
    tool_types = ToolTypeModel.objects.all()
    plot = PlotModel.objects.get_obj()
    if request.method == "POST":
        tool_form = ToolForm(data=request.POST, files=request.FILES)
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
        'plot': plot,
    }
    return render(request, "tools/add_tool.html", context)


def delete_tool(request, tool_id):
    tool = get_object_or_404(ToolModel, id=tool_id)
    tool.delete()
    return HttpResponseRedirect(reverse("tools:index"))


def use_tool(request, tool_id):
    tool = get_object_or_404(ToolModel, id=tool_id)
    task_in_hour = request.GET.get("task_in_hour")
    if task_in_hour:
        task_in_hour = float(request.GET.get("task_in_hour"))
        tool.perform_task(task_in_hour)
    return HttpResponseRedirect(reverse("tools:index"))


def maintain_tool(request, tool_id):
    tool = get_object_or_404(ToolModel, id=tool_id)
    tool.maintenance()
    return HttpResponseRedirect(reverse("tools:index"))
