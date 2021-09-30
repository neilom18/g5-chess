# Generated by Django 3.2.4 on 2021-09-29 22:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_alter_user_usercode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userCode',
            field=models.UUIDField(default=uuid.UUID('c63cc11d-e4a2-4f26-9fba-316317eb1cf8'), unique=True),
        ),
    ]