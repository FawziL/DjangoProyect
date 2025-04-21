from django.shortcuts import render, redirect
from .models import Profesor
from .forms import ProfesorForm

def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores/listar.html', {'profesores': profesores})

def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'profesores/crear.html', {'form': form})

# Implementa similares para actualizar y eliminar