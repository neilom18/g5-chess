from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    país = models.CharField(max_length=100, blank=True,default='')