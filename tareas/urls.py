from django.urls import path
from .views import list_tareas, create_tarea, delete_tarea

urlpatterns = [
    path('', list_tareas),
    path('new/', create_tarea, name='create_tarea'),
    path('delete/<int:tarea_id>/', delete_tarea, name='delete_tarea'),
]
