from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from trains.models import Train
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib import messages
from trains.forms import TrainForm
from django.contrib.messages.views import SuccessMessageMixin

__all__ = ('home', 'TrainDetailView', 'TrainCreateView', 'TrainUpdateView', 'TrainDeleteView', 'TrainListView')


def home(request, pk=None):
    qs = Train.objects.all()
    lst = Paginator(qs, 4)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'trains/home.html', context)


class TrainListView(ListView):
    paginate_by = 4
    model = Train
    template_name = 'trains/home.html'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно создан'


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно отредактирован'


class TrainDeleteView(DeleteView):
    model = Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Поезд успешно удален')
        return super().delete(*args, **kwargs)



