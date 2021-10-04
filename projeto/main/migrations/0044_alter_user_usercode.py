# Generated by Django 3.2.4 on 2021-09-29 22:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_alter_user_usercode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userCode',
            field=models.UUIDField(default=uuid.UUID('247704fd-1242-4047-bc70-e5c55730656b'), unique=True),
        ),
    ]
