from django import db
from django.shortcuts import render
from .serializers import RoomSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Room, User


#Template request
def home(request):
    return render(request, 'home.html')

def lista_salas(request):
    return render(request, 'lista_salas.html')

def sala(request):
    return render(request, 'tabuleiro.html')

def historico(request):
    return render(request, 'historico.html')

def perfil(request):
    return render(request, 'perfil.html')
#Template request


def homeWS(request):
    return render(request,'homeWS.html')

def room(request, room_name):
    return render(request,'roomWS.html',{
        'room_name': room_name
    })