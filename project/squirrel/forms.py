
from django.forms import ModelForm
from squirrel.models import Sighting


class SightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'
