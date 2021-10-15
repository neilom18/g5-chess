from enum import unique
from django.contrib.auth.models import AbstractUser
from django.db import models
import random

import uuid
"""
def ramCode():
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    r = []
    while True:
        for i in range(16):
            i = random.randint(1,2)
            if i == 1:
                n = random.randint(1,9)
                r.append(n)
            else:
                a = random.choice(alph)
                r.append(a)
        r = ''.join(map(str, r))
        for i in fields:
            if r != i:
                pass
            else:
                
    return r
"""

def zerado(x):
        if x == 0:
            return True
        else:
            return False

start = 'rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'

#Rooms
class Room(models.Model):
    roomCode = models.CharField(max_length=10,default=uuid.uuid4(),unique=True,)
    pieces = models.CharField(max_length=len(start), blank=False,null=False, default=start)
    user1 = models.CharField(max_length=150,default='')
    user2 = models.CharField(max_length=150,default='')
    timer1 = models.SmallIntegerField(default=600)
    timer2 = models.SmallIntegerField(default=600)
    tempTimer = models.SmallIntegerField(null=False,default=0)
    whoMove = models.BooleanField(default=True)
    history = models.TextField(default='')



class GameHistory(models.Model):
    result = models.CharField(max_length=1,default='')
    RoomName = models.CharField(max_length=10,default='')
    user1 = models.CharField(max_length=150,default='')
    user2 = models.CharField(max_length=150,default='')
    timer1 = models.SmallIntegerField(default=600)
    timer2 = models.SmallIntegerField(default=600)
    history = models.TextField(default='')


#user
class User(AbstractUser):
    userCode = models.UUIDField(max_length=64,default=uuid.uuid4,unique=True)
    room = models.ForeignKey(Room, related_name = 'room', blank=True,null=True, on_delete = models.CASCADE)


    def __str__(self):
        return self.username

class Relogio(models.Model):
    time = models.DecimalField(max_digits=3, decimal_places=2)
    zero = models.BooleanField(default=zerado(time))


# class Room(models.Model):
#     roomCode = models.UUIDField(max_length=64,default=uuid.uuid4(),unique=True,)
#     pieces = models.CharField(max_length=len(start), blank=False,null=False, default=start)

# #user
# class User(AbstractUser): 
#     userCode = models.UUIDField(max_length=64,default=uuid.uuid4(),unique=True)
#     room = models.ForeignKey(Room, related_name = 'room', null = True,blank=True, on_delete = models.CASCADE)
