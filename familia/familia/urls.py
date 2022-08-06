from django.contrib import admin
from django.urls import path

from familia.views import saludo, plantilla

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='saludo'),
    path('plantilla/', plantilla, name='plantilla'),
]
