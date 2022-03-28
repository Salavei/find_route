from django import forms
from cities.models import City


# class HtmlForm(forms.Form):
#     name = forms.CharField(label='Город')


class CityForm(forms.ModelForm):
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={
        'placeholder': 'Введите название города',
        'class': 'form-control'
    }))

    class Meta:
        model = City
        fields = ('name',)

