from main.views import ramCode
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class Sala(models.Model):
    code = models.CharField(max_length=9, default="0",unique=True)
    d_criacao = models.DateTimeField(auto_now_add=True)

    def sala_code(self):
        return self.code

    def __str__(self):
        return self.code

class User(AbstractUser):
    pais = models.CharField(max_length=100, blank=True,default='')
    id = models.CharField(max_length=16,primary_key=True, default=ramCode())
    sala = models.ForeignKey(Sala, related_name = 'sala', null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.id