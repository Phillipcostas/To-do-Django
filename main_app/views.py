from django.shortcuts import render
from .models import Todo 


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def toDo_index(request):
    toDos = Todo.objects.all()
    return render(request, 'toDo/index.html', {'toDos': toDos})


def toDo_detail(request, toDo_id):
    toDo = Todo.objects.get(id=toDo_id)
    return render(request, 'toDo/detail.html', {'toDo': toDo})


