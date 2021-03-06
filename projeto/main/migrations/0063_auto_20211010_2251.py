# Generated by Django 3.2.4 on 2021-10-11 01:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_auto_20211010_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamehistory',
            name='RoomName',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='room',
            name='roomCode',
            field=models.CharField(default=uuid.UUID('08b8fe53-eaf2-46c9-8214-f568068014b2'), max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userCode',
            field=models.UUIDField(default=uuid.UUID('3a5430fa-f227-4d38-9cc5-f67cb0f19e54'), unique=True),
        ),
    ]
