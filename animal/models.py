from django.db import models
from django.forms import ModelForm
from django.urls import reverse

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=250)
    color = models.CharField(max_length=100)
    type = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('animal:index')


    def __str__(self):
        return self.name + '-' + self.color
