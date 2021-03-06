# Generated by Django 3.2.4 on 2021-09-29 00:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210928_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.UUIDField(default=uuid.UUID('ea7879cb-0fac-4bf6-880c-8671f84c377c'), unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='room',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='room', to='main.room'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userCode',
            field=models.UUIDField(default=uuid.UUID('da1ddd39-89b4-429f-9498-c79d349a08d5'), unique=True),
        ),
    ]
