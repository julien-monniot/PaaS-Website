# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator


class Travel(models.Model):
    author = models.ForeignKey('wu.WuProfil')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    starting_date = models.DateField(blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)
    participants = models.ManyToManyField('wu.WuProfil', through='Participate',
                                          through_fields=('travel', 'person'), related_name='manytomany_user')
    image = models.ImageField(upload_to='images', default='images/road-trip.jpg')
    budget = models.PositiveSmallIntegerField(blank=True, help_text='Bugdet prévisionnel par personne pour le voyage entier',
                                              validators=[MaxValueValidator(limit_value=1000)])

    def __str__(self):
        return self.title+" - "+str(self.created_date)


class Participate(models.Model):
    person = models.ForeignKey('wu.WuProfil')
    travel = models.ForeignKey('travel')
    motivation = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.person)


class Stage(models.Model):
    travel = models.ForeignKey(Travel)
    title = models.CharField(max_length=200)
    point_of_departure = models.CharField(max_length=300)
    point_of_arrival = models.CharField(max_length=300)
    duration = models.PositiveSmallIntegerField(default=1, blank=True, help_text='Durée en jours pour l\'étape',
                                                validators=[MaxValueValidator(limit_value=21)])
    description = models.TextField(blank=True)
    description = models.TextField(blank=True)
