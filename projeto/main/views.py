from django import db
from django.http.response import HttpResponse
from django.shortcuts import render
from .serializers import RoomSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GameHistory, Room, User
from django.db.models import Q

#Template request
def home(request):
    return render(request, 'home.html')


def historico(request):
    return render(request, 'historico.html')

def perfil(request):
    return render(request, 'perfil.html')
#Template request


def homeWS(request):
    return render(request,'homeWS.html')

def room(request, room_name):
    return render(request,'roomWS.html',{
        'room_name': room_name,
    })

def historico(request):
    if request.user.is_authenticated:
        username = str(request.user.username)
        historicos = GameHistory.objects.filter(~Q(history=''),user1=username)
        historicos = historicos,GameHistory.objects.filter(~Q(history=''),user2=username)
        return render(request,'historico.html',{'partidas':historicos})
    else:
        return HttpResponse('<h4>Tu não ta logado animal</h4>')

#teste