# Generated by Django 3.2.4 on 2021-08-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='teste',
            field=models.TextField(blank=True),
        ),
    ]
