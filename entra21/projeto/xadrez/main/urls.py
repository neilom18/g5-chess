from django.urls import path
from .import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('', views.home, name = 'home'),
]