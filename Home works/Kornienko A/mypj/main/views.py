from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from main.models import Volonter, Order
# Create your views here.

class MainView(TemplateView):
    template_name = 'list_volonter.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context.update({
            'Volonters': Volonter.objects.all(),
            'orderss': Order.objects.all(),
        })
        return context

class VolonterListView(ListView):
    template_name = 'list_volonter.html'
    model = Volonter
    context_object_name = 'Volonter'

class VolonterDetailView(DetailView):
    template_name = 'view_volonter.html'
    model = Volonter
    context_object_name = 'Volonter'

class VolonterCreateView(CreateView):
    template_name = 'create_volonter.html'
    model = Volonter
    context_object_name = 'Volonter'
    fields = ('fio','telephone', 'address','birthday', 'gender')
    success_url = reverse_lazy('create_volonter')
class VolonterGrafikView(ListView):
    template_name = 'grafik_volonter.html'
    model = Volonter
    context_object_name = 'Volonter'

class OrderMainView(TemplateView):
    template_name = 'order_list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderMainView, self).get_context_data(**kwargs)
        context.update({
                        'orders': Order.objects.all(),
        })
        return context
class OrderView(ListView):
    template_name = 'order_list.html'
    model = Order
    context_object_name = 'orders'
class OrderDetailView(DetailView):
    template_name = 'view_order.html'
    model = Order
    context_object_name = 'order'
