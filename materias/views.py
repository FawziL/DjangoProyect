from django.shortcuts import render, redirect, get_object_or_404
from .models import Materia
from .forms import MateriaForm

def listar_materias(request):
    materias = Materia.objects.all()
    return render(request, 'materias/listar.html', {'materias': materias})

def crear_materia(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_materias')
    else:
        form = MateriaForm()
    return render(request, 'materias/crear.html', {'form': form})

def editar_materia(request, id):
    materia = get_object_or_404(Materia, id=id)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('listar_materias')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'materias/editar.html', {'form': form})

def eliminar_materia(request, id):
    materia = get_object_or_404(Materia, id=id)
    if request.method == 'POST':
        materia.delete()
        return redirect('listar_materias')
    return render(request, 'materias/eliminar.html', {'materia': materia})