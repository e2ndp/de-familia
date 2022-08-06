from django.contrib import admin
from django.urls import path

from familia.views import saludo, plantilla
from personas.views import create_persona

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='saludo'),
    path('plantilla/', plantilla, name='plantilla'),
    path('new-persona/', create_persona, name='create_persona'),
]
