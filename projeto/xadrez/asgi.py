# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from main.routing import ws_urlpatterns
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xadrez.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            ws_urlpatterns
        )
    ),
})