from django.shortcuts import render
from personas.models import Personas

def create_persona(request):
    new_persona = Personas.objects.create(
        name = 'NASINE, Ezequiel',
        birthday = '1986-08-25',
        cellphone = 150000000
    )
    context = {
        'new_persona' : new_persona
    }
    return render(request, 'new-persona.html', context=context)
