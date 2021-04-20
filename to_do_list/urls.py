from django.urls import path
from django.urls import include
from to_do_list.views import *

urlpatterns = [
    path('', task_list, kwargs = {'mode':'view'}),
    path('add_task', add_task, name='add_task'),
    path('delete_task/<str:task_id>', delete_task, name='delete_task'),
    path('edit_task/<str:task_id>', edit_task, name='edit_task'),
    path('change_task_status/<str:task_id>', change_task_status, name='change_task_status'),
    path('<str:mode>', task_list, name='task_list_url'),
]