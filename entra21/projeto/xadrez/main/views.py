from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sala(request):
    return render(request, 'sala.html')

def historico(request):
    return render(request, 'historico.html')