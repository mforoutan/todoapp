"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.index_view),
    path('delete/<user_id>/<task_pk>', todo_views.delete_task),
    path('deleteall/<user_id>', todo_views.delete_all),
    path('updateStatus/<user_id>/<task_pk>', todo_views.update_task_status),
    path('logout/', todo_views.logout),
    path('login/', todo_views.login),
    path('signup/', todo_views.signup),
]
