from django.shortcuts import render
from .models import Task


def indexView(request):
    if request.user.is_authenticated :
        tasks = Task.objects.filter(user=request.user)
    template = "../templates/index.html"
    context = {
        'tasks': tasks,
    }
    return render(request,template,context)