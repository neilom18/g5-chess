from django.urls import  re_path
from .consumers import RoomConsumer



ws_urlpatterns = [
    re_path(r'ws/room/(?P<room_name>\w+)/$',RoomConsumer.as_asgi()),
]