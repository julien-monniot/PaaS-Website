# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wu', '0003_auto_20151126_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wuprofil',
            name='image',
            field=models.ImageField(upload_to='profile_images', default='profiles-images/nobody.jpg'),
        ),
    ]
