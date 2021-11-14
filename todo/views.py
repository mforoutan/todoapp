from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseRedirect


def indexView(request):
    if request.user.is_authenticated :
        tasks = Task.objects.filter(user=request.user)
        form = TaskForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            return HttpResponseRedirect('/')
            
    template = "../templates/index.html"
    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request,template,context)