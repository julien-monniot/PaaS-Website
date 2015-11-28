# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stage',
            old_name='arrival',
            new_name='point_of_arrival',
        ),
        migrations.RenameField(
            model_name='stage',
            old_name='departure',
            new_name='point_of_departure',
        ),
        migrations.AddField(
            model_name='stage',
            name='duration',
            field=models.PositiveSmallIntegerField(blank=True, help_text="Durée en jours pour l'étape", validators=[django.core.validators.MaxValueValidator(limit_value=21)], default=1),
        ),
        migrations.AlterField(
            model_name='stage',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
