#
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Todo
# import json
# @csrf_exempt
# def tasks(request):
#     if request.method == "GET":
#         data = list(Todo.objects.values())
#         return JsonResponse(data, safe=False)
#     if request.method == "POST":
#         body = json.loads(request.body.decode('utf-8'))
#         Todo.objects.create(
#         title=body["title"],
#         description=body["description"],
#         )
#         return JsonResponse({"message": "POST EXECUTED"})
#
#     if request.method == "PUT":
#         body = json.loads(request.body.decode('utf-8'))
#         task1 = Todo.objects.get(id=body["id"])
#         task1.title = body["title"]
#         task1.description = body["description"]
#         task1.save()
#         return JsonResponse({"message": "PUT EXECUTED"})
#     if request.method == "DELETE":
#         body = json.loads(request.body.decode('utf-8'))
#         task1 = Todo.objects.get(id=body["id"])
#         task1.delete()
#         return JsonResponse({"message": "DELETE EXECUTED"})
#     return JsonResponse({"error": "Method not allowed"}, status=405)

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    counts = {
        "all": tasks.count(),
        "pending": tasks.filter(status="Pending").count(),
        "completed": tasks.filter(status="Completed").count(),
    }
    return render(request, "tasks/task_list.html", {"tasks": tasks, "counts": counts})

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form})

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/edit_task.html", {"form": form, "task": task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("task_list")