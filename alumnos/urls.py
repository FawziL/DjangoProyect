from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alumnos, name='listar_alumnos'),
    path('crear/', views.crear_alumno, name='crear_alumno'),
    path('editar/<int:id>/', views.editar_alumno, name='editar_alumno'),
    path('eliminar/<int:id>/', views.eliminar_alumno, name='eliminar_alumno'),
]