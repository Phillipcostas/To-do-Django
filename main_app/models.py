from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User


class Todo(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("toDo-detail", kwargs={"toDo_id": self.id})

class SubTask(models.Model):
    todo = models.ForeignKey(Todo, related_name='subtasks', on_delete=models.CASCADE)
    task = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
