from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from cities.models import City
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from cities.forms import CityForm

__all__ = ('home', 'CityDetailView', 'CityCreateView', 'CityUpdateView')


def home(request, pk=None):
    form = CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    # if pk:
    # city = City.objects.filter(id=pk).first()
    # city = get_object_or_404(City, id=pk)
    # context = {'object': city}
    # return render(request, 'cities/detail.html', context)

    qs = City.objects.all()
    context = {'object_list': qs, 'form': form}
    return render(request, 'cities/home.html', context)


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    # success_url = '/cities/'
    success_url = reverse_lazy('cities:home')


class CityDetailView(DetailView):
    # model = City
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
