
from django.db import models
from django.forms import ModelForm
from .models import Sighting


class SighingtForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'
