from django.urls import path
from .import views


app_name = 'main'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('lista_salas', views.lista_salas, name= 'lista_salas'),
    path('sala', views.sala, name = 'sala'),
    path('historico', views.historico, name = 'historico'),
    path('perfil', views.perfil, name = 'perfil'),
    path('api/room',views.RoomView),
]