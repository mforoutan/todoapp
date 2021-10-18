from django.db import models
from django.db.models.deletion import CASCADE


class List(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    # def save(self):
    #     if self.title == "":
    #         self.title = "List #{}".format(self.id)

    def __str__(self):
        return self.title

class Task(models.Model):
    text = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=CASCADE, default=1)