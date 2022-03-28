from django import forms
from routes.models import Route
from cities.models import City
from trains.models import Train


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

    # class Meta:
    #     model = Route
    #     fields = '__all__'


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(label='Название маршрута', widget=forms.TextInput(attrs={
        'placeholder': 'Введите название маршрута',
        'class': 'form-control'
    }))
    from_city = forms.ModelChoiceField(
        queryset=City.objects.all(), widget=forms.HiddenInput()
    )
    to_city = forms.ModelChoiceField(
        queryset=City.objects.all(), widget=forms.HiddenInput()
    )
    trains = forms.ModelMultipleChoiceField(
        queryset=Train.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={'class': 'form-control d-none'}
        )
    )
    travel_times = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Route
        fields = '__all__'
