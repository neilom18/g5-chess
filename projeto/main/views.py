from django.shortcuts import render
import random
#Template request
def home(request):
    return render(request, 'home.html')

def lista_salas(request):
    return render(request, 'lista_salas.html')

def sala(request):
    return render(request, 'sala.html')

def historico(request):
    return render(request, 'historico.html')

def perfil(request):
    return render(request, 'perfil.html')
#Template request


def ramCode():
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    r = []
    for i in range(16):
        i = random.randint(1,2)
        if i == 1:
            n = random.randint(1,9)
            r.append(n)
        else:
            a = random.choice(alph)
            r.append(a)
    r = ''.join(map(str, r))
    return r

