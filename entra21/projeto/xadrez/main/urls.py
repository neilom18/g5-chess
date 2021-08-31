from django.urls import path
from django.urls.conf import include
from .import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('sala', views.sala, name = 'sala'),
    path('historico', views.historico, name = 'historico'),
]