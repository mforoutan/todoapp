from django.db.models import query
from django.http.response import HttpResponse
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


def deleteTask(request, id, pk):
    if str(request.user.id) == str(id) and request.user.is_authenticated:
        query = Task.objects.get(pk=pk)
        query.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("Your Access is Unauthorized.")


def deleteAll(request, id):
    if str(request.user.id) == (id) and request.user.is_authenticated:
        query = Task.objects.filter(user=request.user)
        query.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("Your Access is Unauthorized.")