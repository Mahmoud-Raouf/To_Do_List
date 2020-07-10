from django.urls import path
from . import views

urlpatterns = [
    
    path('todo/' , views.todo_list , name='todo'),
    # path('add_todo/' , views.add_todo , name='add_todo'),
    path('update_todo/<int:pk>/' , views.update_todo , name='update_todo'),
    path('todo_delete/<int:pk>/' , views.todo_delete , name='todo_delete'),


    # path('' , views.index , name='index'),
]
