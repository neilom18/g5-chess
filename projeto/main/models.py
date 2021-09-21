from main.views import ramCode
from django.contrib.auth.models import AbstractUser
from django.db import models
from views import ramCode

start = ' rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'


class Room(models.Model):
    code = models.CharField(max_length=10,default="",)
    pieces = models.CharField(max_length=len(start), blank=False,null=False, default=start)


class Sala(models.Model):
    nome = models.CharField(max_length=100, default='sala')
    id = models.CharField(max_length=16,primary_key=True, default=ramCode,unique=True)
    d_criacao = models.DateTimeField(auto_now_add=True)

    def sala_code(self):
        return self.nome

    def __str__(self):
        return self.code

class User(AbstractUser):
    pais = models.CharField(max_length=100, blank=True,default='')
    sala = models.ForeignKey(Sala, related_name = 'sala', null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.id