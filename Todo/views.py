
from django.shortcuts import render
from todoapp.models import Task


def home(request):
    tasks=Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_task=Task.objects.filter(is_completed=True)
    
    context={
        't1':tasks,
        't2':completed_task,
    }
    return render(request,'home.html',context)