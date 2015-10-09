from pyexpat import model
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from Resource.models import Resource


class MainView(TemplateView):
    template_name = 'list_resource.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context.update({
            'Resource': Resource.objects.all(),
        })
        return context
class ResourceListView(ListView):
    template_name = 'list_resource.html'
    model = Resource
    context_object_name = 'Resource'

class ResourceDetailView(DetailView):
    template_name = 'view_resource.html'
    model = Resource
    context_object_name = 'Resource'

class ResourceCreateView(CreateView):
    template_name = 'create_resource.html'
    model = Resource
    context_object_name = 'Resource'
    fields = ('name', 'weight', 'volume','count',)
    success_url = reverse_lazy('create_resource')