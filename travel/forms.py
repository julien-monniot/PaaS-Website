from django import forms
from .models import Travel, Stage
from django.core.validators import MaxValueValidator


class TravelForm(forms.ModelForm):
    title = forms.CharField(max_length=200, help_text="Le titre de votre voyage")
    description = forms.CharField(max_length=1000, help_text="Description du voyage")
    starting_date = forms.DateField()
    ending_date = forms.DateField()
    image = forms.ImageField()
    budget = forms.IntegerField(help_text='Bugdet prévisionnel par personne pour le voyage entier', min_value=0, max_value=1500)

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Travel
        fields = ('title', 'description', 'starting_date', 'ending_date', 'budget', 'image')

class StageForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    point_of_departure = forms.CharField(max_length=300)
    point_of_arrival = forms.CharField(max_length=300)
    duration = forms.IntegerField(help_text='Durée en jours pour l\'étape', max_value=21, min_value=0)
    description = forms.CharField(max_length=1000)

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Stage
        fields = ('title', 'point_of_departure', 'point_of_arrival', 'duration', 'description')