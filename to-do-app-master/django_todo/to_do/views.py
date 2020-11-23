from django.shortcuts import render, redirect
from .models import NewTask
from .forms import TaskForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    tasks = NewTask.objects.all()

    content = {'tasks': tasks}
    return render(request, "to_do/home.html", content)


@login_required
def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit = False)
            task.user = User.objects.get(id = request.user.id)
            task.save()

        messages.success(request, "New task has been created successfully!")    
        return redirect('home')

    form = TaskForm()
    content = {'form': form}

    return render(request, "to_do/new_task.html", content)


def task_view(request, pk):
    task = NewTask.objects.get(id=pk)
    content = {'task': task}
    return render(request, "to_do/task_view.html", content)


def task_update(request, pk):
    task = NewTask.objects.get(id=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

        messages.success(request, "The task has been updated successfully!")        
        return redirect('home')

    form = TaskForm(instance=task)
    content = {'form': form}
    return render(request, "to_do/task_update.html", content)


def task_delete(request, pk):
    task = NewTask.objects.get(id=pk)
    task.delete()

    messages.success(request, "The task has been deleted!")    
    return redirect("home")