from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from urllib.parse import urlencode


from .forms import ToolForm
from .models import ToolModel, ToolTypeModel, ToolStateModel
from plot.models import PlotModel

from src.core.tool import Tool


def index(request):
    tools = ToolModel.objects.all()
    plot = PlotModel.objects.get_obj()

    error_message = request.GET.get('error')
    error_tool_id = request.GET.get('tool_id')
    if error_tool_id:
        try:
            error_tool_id = int(error_tool_id)
        except (ValueError, TypeError):
            error_tool_id = None

    page_number = request.GET.get("page")
    paginator = Paginator(tools, 4)
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "plot": plot,
        "error_message": error_message,
        "error_tool_id": error_tool_id,
    }
    return render(request, "tools/index.html", context)
def add_tool(request):
    tool_types = ToolTypeModel.objects.all()
    plot = PlotModel.objects.get_obj()
    if request.method == "POST":
        tool_form = ToolForm(data=request.POST, files=request.FILES)
        if tool_form.is_valid():
            tool = tool_form.save(commit=False)
            convert_tool = Tool(tool.tool_type, tool.brand, tool.description)
            tool = ToolModel.from_library_tool(convert_tool, plot, tool.image)
            tool.save()
            return HttpResponseRedirect(reverse("tools:index"))
    else:
        tool_form = ToolForm()

    context = {
        "tool_types": tool_types,
        "form": tool_form,
        "plot": plot,
    }
    return render(request, "tools/add_tool.html", context)


def delete_tool(request, tool_id):
    tool = get_object_or_404(ToolModel, id=tool_id)
    tool.delete()
    return HttpResponseRedirect(reverse("tools:index"))


def use_tool(request, tool_id):
    tool = get_object_or_404(ToolModel, id=tool_id)
    task_in_hour = request.GET.get("task_in_hour")
    error = None

    if not task_in_hour:
        error = "Не указано количество часов."
    else:
        try:
            task_in_hour = float(task_in_hour)
            convert_tool = tool.to_library_tool()
            convert_tool.perform_task(task_in_hour)
            tool = tool.update_from_library_tool(convert_tool)
            return redirect(reverse("tools:index"))
        except ValueError:
            error = "Некорректное значение часов. Введите число."
        except Exception as e:
            error = str(e)

    base_url = reverse("tools:index")
    params = urlencode({'error': error, 'tool_id': tool.id})
    return redirect(f"{base_url}?{params}")


def maintain_tool(request, tool_id):
    tool = get_object_or_404(ToolModel, id=tool_id)
    convert_tool = tool.to_library_tool()
    convert_tool.maintenance()
    tool.update_from_library_tool(convert_tool)
    return HttpResponseRedirect(reverse("tools:index"))
