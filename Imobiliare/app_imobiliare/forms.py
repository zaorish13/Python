from django import forms
from .models import RealEstate


class PropertyForm(forms.ModelForm):
    class Meta:
        model = RealEstate
        fields = ['title', 'description', 'price', 'bedrooms', 'bathrooms']
