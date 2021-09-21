from django.shortcuts import render
from .serializers import RoomSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Room

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

#API
@api_view(['GET','POST',])
def RoomView(request):
    if request.method =="GET":
        serializer = RoomSerializer(Room.objects.all(), many=True)
        return Response(serializer.data)


