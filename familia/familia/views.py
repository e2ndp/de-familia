from django.http import HttpResponse

from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Django-Coder")

def plantilla(request):
    return render(request, 'plantilla.html', context={})