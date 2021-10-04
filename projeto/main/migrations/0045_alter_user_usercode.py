# Generated by Django 3.2.4 on 2021-09-29 22:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_alter_user_usercode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userCode',
            field=models.UUIDField(default=uuid.UUID('ae1cb176-30e9-4a59-93a8-f12afba103a4'), unique=True),
        ),
    ]
