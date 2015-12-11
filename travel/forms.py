# -*- coding: utf-8 -*-
from django import forms
from .models import Travel, Stage
from django.forms import inlineformset_factory

MAX_STAGES = 30

StageFormSet = inlineformset_factory(
    Travel,
    Stage,
    extra=1,
    min_num=0,
    max_num=MAX_STAGES,
    fields=('title', 'point_of_departure', 'point_of_arrival', 'duration', 'description'))


class TravelForm(forms.ModelForm):
    title = forms.CharField(max_length=200, label='Titre du Voyage')
    description = forms.CharField(widget=forms.Textarea, max_length=2000, help_text="Description du voyage", label='Description du voyage')
    starting_date = forms.DateField(label='Date de début')
    ending_date = forms.DateField(label='Date de fin')
    image = forms.ImageField(label='Image associée : ')
    budget = forms.IntegerField(help_text='(par personne pour le voyage entier)', min_value=0,
                                max_value=1500, label='Bugdet prévisionnel')

    class Meta:
        model = Travel
        fields = ('title', 'description', 'starting_date', 'ending_date', 'budget', 'image')


class StageForm(forms.ModelForm):
    title = forms.CharField(max_length=200, label='Nom de l\'étape')
    point_of_departure = forms.CharField(max_length=300, label='Point de départ')
    point_of_arrival = forms.CharField(max_length=300, label='Point d\'arrivée')
    duration = forms.IntegerField(help_text='(en jours)', max_value=21, min_value=0, label='Durée')
    description = forms.CharField(widget=forms.Textarea, max_length=2000, label='')

    class Meta:
        model = Stage
        fields = ('title', 'point_of_departure', 'point_of_arrival', 'duration', 'description')
