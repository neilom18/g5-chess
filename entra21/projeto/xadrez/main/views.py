from django.shortcuts import render
import random

def home(request):
    return render(request, 'home.html')

def lista_salas(request):
    return render(request, 'lista_salas.html')

def sala(request):
    return render(request, 'sala.html')

def historico(request):
    return render(request, 'historico.html')



