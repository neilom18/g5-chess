# Generated by Django 3.2.4 on 2021-09-24 18:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_user_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pais',
        ),
        migrations.AlterField(
            model_name='user',
            name='userCode',
            field=models.UUIDField(default=uuid.uuid1, unique=True),
        ),
    ]
