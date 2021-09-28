# Generated by Django 3.2.4 on 2021-09-24 15:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210920_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sala',
        ),
        migrations.AddField(
            model_name='user',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room', to='main.room'),
        ),
        migrations.AddField(
            model_name='user',
            name='userCode',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='pieces',
            field=models.CharField(default=' rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77', max_length=160),
        ),
        migrations.DeleteModel(
            name='Sala',
        ),
    ]