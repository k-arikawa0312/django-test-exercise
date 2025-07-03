from django.shortcuts import render
from django.timezone import make_aware
from django.utils.dateparse import parse_datetime
from todo.models import Task

# Create your views here.
def index(request):
    if request.method == 'POST':
        task=Task(title=request.POST['title'],due_at=parse_datetime(request.POST['due_at']))
        task.save()
    
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
    }

    return render(request, 'todo/index.html', context)