# Generated by Django 3.2.4 on 2021-10-10 18:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_merge_0054_auto_20211001_1012_0058_auto_20210930_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='tempTimer',
            field=models.SmallIntegerField(default=600),
        ),
        migrations.AddField(
            model_name='room',
            name='timer1',
            field=models.SmallIntegerField(default=600),
        ),
        migrations.AddField(
            model_name='room',
            name='timer2',
            field=models.SmallIntegerField(default=600),
        ),
        migrations.AlterField(
            model_name='room',
            name='roomCode',
            field=models.CharField(default=uuid.UUID('b765ded1-209f-4a1a-b5f3-74de916eb5bb'), max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userCode',
            field=models.UUIDField(default=uuid.UUID('1ba27103-fa40-447f-843b-2b2182b61993'), unique=True),
        ),
    ]
