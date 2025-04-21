from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_materias, name='listar_materias'),
    path('crear/', views.crear_materia, name='crear_materia'),
    path('editar/<int:id>/', views.editar_materia, name='editar_materia'),
    path('eliminar/<int:id>/', views.eliminar_materia, name='eliminar_materia'),
]