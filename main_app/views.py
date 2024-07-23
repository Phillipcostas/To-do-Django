from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def toDo_index(request):
    return render(request, 'toDo/index.html', {'toDo': toDo})


class Todo:
    def __init__(self, name, description):
        self.name = name 
        self.description = description

toDo = [
    Todo('take out trash', 'take the trash out'),
    Todo('clean the fridge', 'clean the fridge'),
    Todo('take out trash', 'take the trash out'),
    Todo('take out trash', 'take the trash out'),
]