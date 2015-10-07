from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from main.models import Volonter, Direction, Transport, GeographyPoint, Order, Need


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
              'telephone', 'gender',)
    success_url = reverse_lazy('create_volonters')

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
    success_url = reverse_lazy('create_direction')

#//////////////////////////////////////////////////Transport////////////////////////////////////////////////////////////

class TransportMainView(TemplateView):
    template_name = 'list_transport.html'

    def get_context_data(self, **kwargs):
        context = super(TransportMainView, self).get_context_data()
        context.update({'transports': Transport.objects.all})
        return context

class TransportListView(ListView):
    template_name = 'list_transport.html'
    model = Transport
    context_object_name = 'transport'

class TransportDetailView(DetailView):
    template_name = 'view_transport.html'
    model = Transport
    context_object_name = 'transport'

#/////////////////////////////////////////////////geographyPoint////////////////////////////////////////////////////////
class GPointMainView(TemplateView):
    template_name = 'list_transport.html'

    def get_context_data(self, **kwargs):
        context = super(GPointMainView, self).get_context_data()
        context.update({'gPoints': GeographyPoint.objects.all()})
        return context
class GPointListView(ListView):
    template_name = 'list_geographyPoint.html'
    model = GeographyPoint
    context_object_name = 'gPoint'

class GPointDetailView(DetailView):
    template_name = 'view_geography.html'
    model = GeographyPoint
    context_object_name = 'gPoint'
#///////////////////////////////////////////////////resources///////////////////////////////////////////////////////////

#////////////////////////////////////////////////////order//////////////////////////////////////////////////////////////
class OrderMainView(TemplateView):
    template_name = 'list_order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderMainView, self).get_context_data()
        context.update({'orders':Order.objects.all()})
        return context

class OrderListView(ListView):
    template_name = 'list_order.html'
    model = Order
    context_object_name = 'order'

class OrderDetailView(DetailView):
    template_name = 'view_order.html'
    model = Order
    context_object_name = 'order'

#/////////////////////////////////////////////needs////////////////////////////////////////////////////////////////////////

class NeedMainView(TemplateView):
    template_name = 'list_need.html'

    def get_context_data(self, **kwargs):
        context = super(NeedMainView, self).get_context_data()
        context.update({'needs':Need.objects.all()})
        return context

class NeedListView(ListView):
    template_name = 'list_need.html'
    model = Need
    context_object_name = 'need'

class NeedDetailView(DetailView):
    template_name = 'view_need.html'
    model = Need
    context_object_name = 'need'





















