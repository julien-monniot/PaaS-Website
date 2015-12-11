# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20151128_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='description',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='travel',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
