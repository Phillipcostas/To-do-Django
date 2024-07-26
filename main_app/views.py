from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo, SubTask 
from .forms import TodoForm, SubTaskFormSet
from django.forms import modelformset_factory
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def toDo_index(request):
    toDos = Todo.objects.filter(user=request.user)
    return render(request, 'toDo/index.html', {'toDos': toDos})

@login_required
def toDo_detail(request,pk, toDo_id):
    toDo = Todo.objects.get(id=toDo_id)
    if request.method == 'POST':
        toDo = Todo.objects.filter(user=request.user)
        for subtask in toDo.subtasks.all():
            subtask.completed = f'subtask_{subtask.id}' in request.POST
            subtask.save()
        return redirect(reverse('toDo-detail', args=[pk]))

    # return render(request, 'toDo/detail.html', {'toDo': toDo})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('toDo-index')
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


    
class TodoCreate(LoginRequiredMixin, CreateView):
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

class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_form.html' 
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('toDo-update', kwargs = {'pk': pk})
        

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

class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = '/toDo'


class Home(LoginView):
    template_name = 'home.html'

    
        