# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_auto_20151208_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='participants',
            field=models.ManyToManyField(to='wu.WuProfil', through='travel.Participate', related_name='manytomany_user', blank=True),
        ),
    ]
