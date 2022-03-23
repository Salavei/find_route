from django.shortcuts import render, get_object_or_404

from cities.models import City
from django.views.generic import DetailView

__all__ = ('home', 'CityDetailView')


def home(request, pk=None):
    if pk:
        # city = City.objects.filter(id=pk).first()
        city = get_object_or_404(City, id=pk)
        context = {'object': city}
        return render(request, 'cities/detail.html', context)
    qs = City.objects.all()
    context = {'object_list': qs}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    # model = City
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

