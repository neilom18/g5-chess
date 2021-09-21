from django.contrib.auth.models import AbstractUser
from django.db import models



start = ' rw00 cw10 bw20 qw30 kw40 bw50 cw60 rw70 pw01 pw11 pw21 pw31 pw41 pw51 pw61 pw71 pb06 pb16 pb26 pb36 pb46 pb56 pb66 pb76 rb07 cb17 bb27 qb37 kb47 bb57 cb67 rb77'

class Room(models.Model):
    code = models.CharField(max_length=10,default="",)
    pieces = models.CharField(max_length=len(start), blank=False,null=False, default=start)


class Sala(models.Model):
    code = models.CharField(max_length=9, default="0",unique=True)
    d_criacao = models.DateTimeField(auto_now_add=True)

    def sala_code(self):
        return self.code

    def __str__(self):
        return self.code

class User(AbstractUser):
    pais = models.CharField(max_length=100, blank=True,default='')
    sala = models.ForeignKey(Sala, related_name = 'sala', null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.id