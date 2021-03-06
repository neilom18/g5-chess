# Generated by Django 3.2.4 on 2021-09-29 22:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20210929_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='roomCode',
            field=models.UUIDField(default=uuid.UUID('a4c34b56-753f-4fc3-9dc3-593023f45a37'), unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userCode',
            field=models.UUIDField(default=uuid.UUID('a0031631-35db-4bef-bdda-a6166a4ffa4a'), unique=True),
        ),
    ]
