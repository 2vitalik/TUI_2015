from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.base import TemplateView
from storehouse.models import StoreHouse


# class MainView(TemplateView):
#     template_name = 'list_storehouse.html'
#
#     def get_context_data(self, **kwargs):
#         context= super(MainView, self).get_context_data(**kwargs)
#         context.update({
#             'StoreHouses':StoreHouse.objects.all()
#         })
#
#
# class StoreHouseListView(ListView):
#     template_name = 'list_storehouse.html'
#     model = StoreHouse
#     context_object_name = 'StoreHouses'
#
#
# class StoreHouseDetailView(DetailView):
#    template_name = 'view_storehouse.html'
#    model = StoreHouse
#    context_object_name = 'StoreHouses'
#
# class StoreHouseCreateView(CreateView):
#     template_name = 'create_storehouse.html'
#     model = StoreHouse
#     context_object_name = 'StoreHouse'
#     fields = ('X', 'Y', 'V', 'Adress')
#     success_url = reverse_lazy('list_StoreHouse')
#
# class StoreHouseUpdateView(UpdateView):
#     template_name = 'update_storehouse.html'
#     model = StoreHouse
#     context_object_name = 'StoreHouse'
#     fields = ('X', 'Y', 'V', 'Adress')
#     success_url = reverse_lazy('list_StoreHouse')

# Create your views here.
