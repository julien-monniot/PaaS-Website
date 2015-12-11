# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class WuProfil(models.Model):
    user = models.OneToOneField(User)
    promo = models.PositiveSmallIntegerField(help_text='L\'année de fin du cursus INSA',
                                             validators=[MaxValueValidator(limit_value=2050),
                                                         MinValueValidator(limit_value=2014)])
    city = models.CharField(blank=True,max_length=150, help_text='Ville actuelle')
    can_welcome_people = models.BooleanField(default=False, blank=True,
                                             help_text='Possibilité d\'accueillir des WUs en transit')
    image = models.ImageField(upload_to='profile_images', default='profile_images/nobody.jpg')

    def __str__(self):
        return self.user.username