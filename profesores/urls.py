from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_profesores, name='listar_profesores'),
    path('crear/', views.crear_profesor, name='crear_profesor'),
]