from django.db import models
from django.db.models.deletion import CASCADE


class Task(models.Model):
    text = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


class List(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    tasks = models.ForeignKey(Task, on_delete=CASCADE)
