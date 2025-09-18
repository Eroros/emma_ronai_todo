from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    active_tasks = Task.objects.filter(completed=False).order_by('-added_on')
    completed_tasks = Task.objects.filter(completed=True).order_by('-added_on')

    return render(
        request,
        'tasks/task_list.html',
        {'form': form, 'active_tasks': active_tasks, 'completed_tasks': completed_tasks}
    )

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')