from django import forms
from routes.models import Route
from cities.models import City


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control js-example-basic-single'
    }))
    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control js-example-basic-single'
    }))
    cities = forms.ModelMultipleChoiceField(label='Через города', queryset=City.objects.all(), required=False,
                                            widget=forms.SelectMultiple(attrs={
                                                'class': 'form-control js-example-basic-multiple'}))
    travelling_time = forms.IntegerField(label='Время в пути', widget=forms.NumberInput(attrs={
        'placeholder': 'время в пути',
        'class': 'form-control'
    }))

    class Meta:
        model = Route
        fields = '__all__'
