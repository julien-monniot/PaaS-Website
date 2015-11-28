from django import forms
from .models import WuProfil
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = WuProfil
        fields = ['promo', 'city', 'can_welcome_people', 'image']

