# Generated by Django 3.2.4 on 2021-10-01 13:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_auto_20210930_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='history',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='userCode',
            field=models.UUIDField(default=uuid.UUID('f9049e02-fc5e-4fbf-a1fc-e559bb1b65a0'), unique=True),
        ),
    ]
