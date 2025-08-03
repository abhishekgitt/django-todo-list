from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo


# To get all tasks
def get_all_tasks():
    return Todo.objects.all().order_by('-created_at')


# Home page view — handle POST & GET ,  manuplate data & send data to html.
def home(request):
    tasks = get_all_tasks()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_todo')
    else:
        form = TodoForm()
    return render(request, 'todo/home.html', {'form': form, 'tasks': tasks})


# Edit a specific task by ID
def edit_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    tasks = get_all_tasks()

    if request.method == 'POST': 
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home_todo')
    else:
        form = TodoForm(instance=task)
    #return these data to html file 
    return render(request, 'todo/home.html', {
        'form': form,
        'tasks': tasks,
        'edit': True,
        'task_id': task_id
    })


# Delete a task by ID
def delete_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    task.delete()
    return redirect('home_todo')
