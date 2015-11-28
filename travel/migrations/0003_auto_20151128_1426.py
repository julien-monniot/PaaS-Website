# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20151128_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='budget',
            field=models.PositiveSmallIntegerField(help_text='Bugdet prévisionnel par personne pour le voyage entier', blank=True, validators=[django.core.validators.MaxValueValidator(limit_value=1000)]),
        ),
    ]
