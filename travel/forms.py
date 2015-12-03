from django import forms
from .models import Travel, Stage
from django.core.validators import MaxValueValidator


class TravelForm(forms.ModelForm):
    title = forms.CharField(max_length=200, help_text="Le titre de votre voyage")
    description = forms.TextField(help_text="Description du voyage")
    starting_date = forms.DateField(blank=True, null=True)
    ending_date = forms.DateField(blank=True, null=True)
    image = forms.ImageField(upload_to='images', default='images/road-trip.jpg')
    budget = forms.PositiveSmallIntegerField(blank=True, help_text='Bugdet prévisionnel par personne pour le voyage entier',
                                              validators=[MaxValueValidator(limit_value=1000)])

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    fields = ('title', 'description', 'starting_date', 'ending_date', 'budget', 'image')

    class Meta:
        model = Travel


class StageForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    point_of_departure = forms.CharField(max_length=300)
    point_of_arrival = forms.CharField(max_length=300)
    duration = forms.PositiveSmallIntegerField(default=1, blank=True, help_text='Durée en jours pour l\'étape',
                                                validators=[MaxValueValidator(limit_value=21)])
    description = forms.TextField(blank=True)

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Stage
        fields = ('title', 'point_of_departure', 'point_of_arrival', 'duration', 'description')