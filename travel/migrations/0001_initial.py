# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wu', '0005_auto_20151126_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('motivation', models.PositiveSmallIntegerField()),
                ('person', models.ForeignKey(to='wu.WuProfil')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('departure', models.CharField(max_length=300)),
                ('arrival', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('starting_date', models.DateField(null=True, blank=True)),
                ('ending_date', models.DateField(null=True, blank=True)),
                ('image', models.ImageField(upload_to='images', default='images/road-trip.jpg')),
                ('budget', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=1000)], help_text='Bugdet prévisionnel par personne pour le voyage entier')),
                ('author', models.ForeignKey(to='wu.WuProfil')),
                ('participants', models.ManyToManyField(through='travel.Participate', related_name='manytomany_user', to='wu.WuProfil')),
            ],
        ),
        migrations.AddField(
            model_name='stage',
            name='travel',
            field=models.ForeignKey(to='travel.Travel'),
        ),
        migrations.AddField(
            model_name='participate',
            name='travel',
            field=models.ForeignKey(to='travel.Travel'),
        ),
    ]
