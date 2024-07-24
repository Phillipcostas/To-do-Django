from django.db import models
from django.urls import reverse 


class Todo(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default = False)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("toDo-detail", kwargs={"toDo_id": self.id})


