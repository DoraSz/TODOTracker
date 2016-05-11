from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Task
from datetime import date
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.order_by('deadline')	# query set: alle Aufgaben, geordnet nach Deadline
    
	# adding extra 'meter-property' to task object to fill meter tag with value between 0 and 1
	# adding another extra 'context-property' to indicate success/danger contextual bootstraps classes
    for task in tasks:
        task.meter = lambda: None
        task.context = lambda: None
        setattr(task, 'meter', (task.state/100))
        if task.state == 100:
            setattr(task, 'context', 'succes')
        elif task.deadline < date.today():
            setattr(task, 'context', 'danger')
        else:
            setattr(task, 'context', 'none')
			
    return render(request, 'todotracker/task_list.html', {'tasks': tasks})		# tasks wird dem Template übergeben, task_list.html wird zurückgegeben
	
def impressum(request):
    return render(request, 'todotracker/impressum.html', {})	# impressum wird zurückgegeben
	
def new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return task_list(request)
    else:
        form = TaskForm()
    return render(request, 'todotracker/new.html', {'form': form})
	
def edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return task_list(request)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todotracker/edit.html', {'form': form})
	
def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return task_list(request)
	
	
	