# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_auto_20151208_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='image',
            field=models.ImageField(upload_to='images', default='images/road-trip.jpg', blank=True),
        ),
    ]
