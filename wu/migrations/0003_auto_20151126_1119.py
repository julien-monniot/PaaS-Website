# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wu', '0002_auto_20151126_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wuprofil',
            name='image',
            field=models.ImageField(upload_to='profile_images', default='nobody.jpg'),
        ),
        migrations.AlterField(
            model_name='wuprofil',
            name='promo',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=2050), django.core.validators.MinValueValidator(limit_value=2014)], help_text="L'année de fin du cursus INSA"),
        ),
    ]
