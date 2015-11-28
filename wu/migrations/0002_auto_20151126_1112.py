# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wuprofil',
            name='image',
            field=models.ImageField(upload_to='profile_images', default='images/nobody.jpg'),
        ),
        migrations.AlterField(
            model_name='wuprofil',
            name='promo',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=2050), django.core.validators.MinValueValidator(limit_value=2014)], blank=True, help_text="L'année de fin du cursus INSA"),
        ),
    ]
