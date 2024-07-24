from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo 
from .forms import TodoForm


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



class TodoCreate(CreateView):
    model = Todo 
    form_class = TodoForm
    template_name = 'toDo/form.html'
    fields = '__all__'
    success_url = '/toDo'

class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'toDo/form.html' 
    fields = '__all__'
    success_url = '/toDo'

class TodoDelete(DeleteView):
    model = Todo
    success_url = '/toDo'