from django.urls import path
from .consumers import RoomConsumer



ws_urlpatterns = [
    path('ws/room/', RoomConsumer.as_asgi())
]