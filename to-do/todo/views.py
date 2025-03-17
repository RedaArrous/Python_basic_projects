from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from django.db.models import F


def index(request):
    task = Task.objects.order_by("-date_added")
    context = {'tasks': task}
    # for deleting todo
    if 'delete' in request.GET:
        task_id = request.GET['delete']
        Task.objects.get(id=task_id).delete()
        return redirect('todo:index')

    # for adding todo
    if 'add' in request.POST:
        new_task = Task()
        new_task.task_name = request.POST['task_name']
        new_task.category = request.POST['category']
        new_task.importancy = request.POST['importancy']
        new_task.save()
        return redirect('todo:index')

    return render(request, 'todo/index.html', context)

def add(request):
    if 'Cancle' in request.POST:
        return redirect("todo:index")
    return render(request, 'todo/add.html')

def edit(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.category = request.POST['category']
        task.importancy = request.POST['importancy']
        task.save()
        return redirect('todo:index')

    return render(request, 'todo/edit.html', {'task': task})
