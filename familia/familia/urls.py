from django.contrib import admin
from django.urls import path

from familia.views import saludo, plantilla
from personas.views import create_persona, list_personas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='saludo'),
    path('plantilla/', plantilla, name='plantilla'),
    path('new-persona/', create_persona, name='create_persona'),
    path('list-personas/', list_personas, name='list_personas'),
]
