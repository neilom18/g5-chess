from django.contrib.auth.models import AbstractUser
from django.db import models



start = ' rwa1 cwb1 bwc1 qwd1 kwe1 bwf1 cwg1 rwh1 pwa2 pwb2 pwc2 pwd2 pwe2 pwf2 pwg2 pwh2 pba7 pbb7 pbc7 pbd7 pbe7 pbf7 pbg7 pbh7 rba8 cbb8 qbd8 kbe8 bbf8 cbg8 rbh8'

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