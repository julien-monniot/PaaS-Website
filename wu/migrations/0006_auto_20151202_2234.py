# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wu', '0005_auto_20151126_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wuprofil',
            name='image',
            field=models.ImageField(upload_to='profile_images', default='profile_images/nobody.jpg'),
        ),
    ]
