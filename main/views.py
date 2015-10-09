from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from main.models import Volonter, Direction


class MainView(TemplateView):
    template_name = 'list_volonter.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context.update({
            'volonters': Volonter.objects.all(),
        })
        return context


class VolonterListView(ListView):
    template_name = 'list_volonter.html'
    model = Volonter
    context_object_name = 'volonters'

class VolonterDetailView(DetailView):
    template_name = 'view_volonter.html'
    model = Volonter
    context_object_name = 'volonter'

class VolonterCreateView(CreateView):
    template_name = 'create_volonter.html'
    model = Volonter
    fields = ('fio', 'address',
              'telephone', 'gender')
    success_url = reverse_lazy('list_volonters')

class VolonterUpdateView(UpdateView):
    template_name = 'update_volonter.html'
    model = Volonter
    context_object_name = 'volonter'
    fields = ('fio', 'address',
              'telephone', 'gender')

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class DirectionMainView(TemplateView):
    template_name = 'list_directions.html'
    def get_context_data(self, **kwargs):
        context = super(DirectionMainView, self).get_context_data(**kwargs)
        context.update({
            'directions': Direction.objects.all(),
        })
        return context

class DirectionListView(ListView):
    template_name = 'list_directions.html'
    model = Direction
    context_object_name = 'directions'

class DirectionDetailView(DetailView):
    template_name = 'view_directions.html'
    model = Direction
    context_object_name = 'direction'

class DirectionUpdateView(UpdateView):
    template_name = 'update_directions.html'
    model = Direction
    context_object_name = 'direction'
    fields = ('name', 'importance',)

class DirectionCreateView(CreateView):
    template_name = 'create_direction.html'
    model = Direction
    fields = ('name', 'importance',)
    success_url = reverse_lazy('list_directions')

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

