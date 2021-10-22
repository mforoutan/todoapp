from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    text = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "Task: {} from User: {}".format(self.text, self.user.username)