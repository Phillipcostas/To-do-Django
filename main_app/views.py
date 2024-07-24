from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo, SubTask 
from .forms import TodoForm, SubTaskFormSet
from django.forms import modelformset_factory



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def toDo_index(request):
    toDos = Todo.objects.all()
    return render(request, 'toDo/index.html', {'toDos': toDos})


def toDo_detail(request, toDo_id):
    toDo = Todo.objects.get(id=toDo_id)
    subtasks = SubTask.objects.filter(todo=toDo)
    return render(request, 'toDo/detail.html', {'toDo': toDo})

    
class TodoCreate(CreateView):
    model = Todo 
    form_class = TodoForm
    template_name = 'todo_form.html'
    success_url = '/toDo'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['subtasks'] = SubTaskFormSet(self.request.POST)
        else:
            data['subtasks'] = SubTaskFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        subtasks = context['subtasks']
        self.object = form.save()
        if subtasks.is_valid():
            subtasks.instance = self.object
            subtasks.save()
        return super().form_valid(form)

class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_form.html' 
    success_url = '/toDo'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['subtasks'] = SubTaskFormSet(self.request.POST, instance=self.object)
        else:
            data['subtasks'] = SubTaskFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        subtasks = context['subtasks']
        self.object = form.save()
        if subtasks.is_valid():
            subtasks.instance = self.object
            subtasks.save()
        return super().form_valid(form)

class TodoDelete(DeleteView):
    model = Todo
    success_url = '/toDo'