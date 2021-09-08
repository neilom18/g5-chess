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

def random_code():
    r = []
    for i in range(9):
        i = random.randint(0,9)
        r.append(i)
    r_code = ''.join(map(str, r))
    return r_code
