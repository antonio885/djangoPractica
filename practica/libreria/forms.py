from django import forms

from .models import superheroe


class libroFrom(forms.ModelForm):
    class Meta: 
        model = superheroe
        fields = '__all__'