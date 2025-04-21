from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('profesores/', include('profesores.urls')),
    path('materias/', include('materias.urls')),
    path('alumnos/', include('alumnos.urls')),
]
