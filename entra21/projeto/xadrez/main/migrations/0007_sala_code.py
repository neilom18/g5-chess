# Generated by Django 3.2.4 on 2021-09-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_sala_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='code',
            field=models.CharField(default='', max_length=9, unique=True),
        ),
    ]
