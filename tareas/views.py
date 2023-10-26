from django.shortcuts import render, redirect
from .models import Tarea


def list_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'list_tareas.html', {'tareas': tareas})


def create_tarea(request):
    tarea = Tarea(title=request.POST['title'],
                  description=request.POST['description'])
    tarea.save()
    return redirect('/tareas/')


def delete_tarea(request, tarea_id):
    delete_tarea = Tarea.objects.get(id=tarea_id)
    delete_tarea.delete()
    return redirect('/tareas/')
