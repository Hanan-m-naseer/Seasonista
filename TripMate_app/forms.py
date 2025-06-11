from django import forms
from .models import Destination, DestinationImage

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['place_name', 'weather', 'state', 'district', 'google_map_link', 'description']

class DestinationImageForm(forms.ModelForm):
    class Meta:
        model = DestinationImage
        fields = ['image']
