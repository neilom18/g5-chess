from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class User(AbstractUser):
    pais = models.CharField(max_length=100, blank=True,default='')
