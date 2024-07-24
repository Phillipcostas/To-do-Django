from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('toDo', views.toDo_index, name='toDo-index'),
    path('toDo/<int:toDo_id>/', views.toDo_detail, name='toDo-detail'),
    path('todo/create/', views.TodoCreate.as_view(), name='toDo-create'),
    path('todo/<int:pk>/update/', views.TodoUpdate.as_view(), name='toDo-update'),
    path('todo/<int:pk>/delete/', views.TodoDelete.as_view(), name='toDo-delete'),

]
