from multiprocessing import context
from django.shortcuts import render
from personas.models import Personas

def create_persona(request):
    new_persona = Personas.objects.create(
        name = 'NASINE, Cinthya',
        birthday = '1991-03-25',
        cellphone = 150000002
    )
    context = {
        'new_persona' : new_persona
    }
    return render(request, 'new-persona.html', context=context)

def list_personas(request):
    personas = Personas.objects.all()
    context = {
        'personas' : personas
    }
    return render(request, 'list-personas.html', context=context)