# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WuProfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('promo', models.PositiveSmallIntegerField(help_text="L'année de fin du cursus INSA", validators=[django.core.validators.MaxValueValidator(limit_value='2014'), django.core.validators.MinValueValidator(limit_value='2050')], blank=True)),
                ('city', models.CharField(max_length=150, help_text='Ville actuelle', blank=True)),
                ('can_welcome_people', models.BooleanField(default=False, help_text="Possibilité d'accueillir des WUs en transit")),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
