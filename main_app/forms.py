from django import forms
from .models import Todo, SubTask 
from django.forms.models import inlineformset_factory


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['name', 'completed']

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

SubTaskFormSet = inlineformset_factory(Todo, SubTask, form=SubTaskForm, extra=1)
