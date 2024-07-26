To-do's

Trello - https://trello.com/b/DwXJ8n2K/django-traveling-app

Attributions -
    - Stack Overflow - (https://stackoverflow.co/teams/?utm_source=adwords&utm_medium=ppc&utm_campaign=kb_teams_search_nb_dsa_targeted_audiences_namer&_bt=608707708707&_bk=&_bm=&_bn=g&gad_source=1&gclid=CjwKCAjwko21BhAPEiwAwfaQCGpQkNfItVodSc_IGI5Q2jhVV2EMX17-VzjGJ2p6Sk5Jg9upcIge6hoCW7oQAvD_BwE)
    
    - 

Technologies used: 
    - Django 
    - PostgreSQL 
    - Javascript
    - Python 
    - HTML 
    - CSS 

Future Expansion Plans 
    - Add a calendar 
    - Update the cross out feature to be updated automatically 
    - 

def toDo_update_view(request, pk):
   
    if request.method == 'POST':
        toDo = Todo.objects.filter(user=request.user)
        for subtask in toDo.subtasks.all():
            subtask.completed = f'subtask_{subtask.id}' in request.POST
            subtask.save()
        return redirect(reverse('toDo-detail', args=[pk]))

    return render(request, 'toDo/detail.html', {'toDo': toDo})