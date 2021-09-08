from django.contrib.auth.models import AbstractUser
from django.db import models
from .import views

class User(AbstractUser):
    pais = models.CharField(max_length=100, blank=True,default='')

class Sala(models.Model):
    code = views.random_code()
    user = models.ForeignKey(User, related_name = 'user', null = False, on_delete = models.CASCADE)

    def __str__(self):
        return self.code

