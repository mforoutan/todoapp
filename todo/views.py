from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Task
from .forms import LoginForm, TaskForm, SignupForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as django_logout, login as django_login
from django.contrib.auth import authenticate


def index_view(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('status')
        pending_tasks = Task.objects.filter(user=request.user, status=False)
        pending_tasks = pending_tasks.count()
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
            'pendingTasks': pending_tasks,
        }
        return render(request, template, context)
    else:
        return HttpResponseRedirect('login/')


def delete_task(request, user_id, task_pk):
    if str(request.user.id) == str(user_id) and request.user.is_authenticated:
        query = Task.objects.get(pk=task_pk)
        query.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("<p>Your Access is Unauthorized.<br><a href='/'>Back to the Homepage</a></p>")


def delete_all(request, user_id):
    if str(request.user.id) == str(user_id) and request.user.is_authenticated:
        query = Task.objects.filter(user=request.user)
        query.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("<p>Your Access is Unauthorized.<br><a href='/'>Back to the Homepage</a></p>")


def update_task_status(request, user_id, task_pk):
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


def login(request):
    form = LoginForm(request.POST)
    template = '../templates/login.html'
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
        return HttpResponseRedirect('/')

    context = {
        'form': form,
    }
    return render(request, template, context)


def signup(request):
    form = SignupForm(request.POST)
    template = '../templates/signup.html'
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        django_login(request, user)
        return HttpResponseRedirect('/')
    return render(request, template, {'form': form})
