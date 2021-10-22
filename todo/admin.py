from django.contrib import admin
from django.contrib.admin.decorators import action
from django.contrib.admin.options import ModelAdmin
from .models import Task


@admin.action(description="Mark tasks as complete.")
def complete_tasks(modeladmin, request, queryset):
    queryset.update(status=True)

class taskModelAdmin(ModelAdmin):
    list_display = ['text', 'user', 'created_on', 'status']
    actions = [complete_tasks]

admin.site.register(Task, taskModelAdmin)