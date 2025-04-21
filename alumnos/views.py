from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno
from .forms import AlumnoForm

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/listar.html', {'alumnos': alumnos})

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/crear.html', {'form': form})

def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumnos/editar.html', {'form': form})

def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.delete()
        return redirect('listar_alumnos')
    return render(request, 'alumnos/eliminar.html', {'alumno': alumno})