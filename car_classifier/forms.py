# car_classifier/forms.py
from django import forms
from .models import CarImage

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image']
