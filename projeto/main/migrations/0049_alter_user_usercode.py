# Generated by Django 3.2.4 on 2021-09-29 23:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_merge_20210929_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userCode',
            field=models.UUIDField(default=uuid.UUID('3ea4229a-3b2a-409f-8c93-e56cee2376b0'), unique=True),
        ),
    ]
