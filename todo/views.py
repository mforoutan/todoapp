from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as django_logout


def indexView(request):
    if request.user.is_authenticated :
        tasks = Task.objects.filter(user=request.user).order_by('status')
        pendingTasks = Task.objects.filter(user=request.user,status=False)
        pendingTasks = pendingTasks.count()
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
            'pendingTasks': pendingTasks,
        }
        return render(request,template,context)
    else:
        return HttpResponseRedirect('login/')


def deleteTask(request, user_id, task_pk):
    if str(request.user.id) == str(user_id) and request.user.is_authenticated:
        query = Task.objects.get(pk=task_pk)
        query.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("<p>Your Access is Unauthorized.<br><a href='/'>Back to the Homepage</a></p>")


def deleteAll(request, user_id):
    if str(request.user.id) == str(user_id) and request.user.is_authenticated:
        query = Task.objects.filter(user=request.user)
        query.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("<p>Your Access is Unauthorized.<br><a href='/'>Back to the Homepage</a></p>")


def taskUpdateStatus(request, user_id, task_pk):
    if str(request.user.id) == str(user_id) and request.user.is_authenticated:
        query = Task.objects.get(pk=task_pk)
        query.status = True
        query.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("<p>Your Access is Unauthorized.<br><a href='/'>Back to the Homepage</a></p>")


def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')