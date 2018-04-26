from django import forms
from django.contrib.auth.models import User
from .models import Animal

class AnimalForm(forms.ModelForm):

    class Meta:
        models = Animal
        fields = ['name', 'color', 'type']