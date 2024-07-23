from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('toDo', views.toDo_index, name='toDo-index'),
]
