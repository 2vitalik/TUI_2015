# coding: utf-8
from httplib import HTTPResponse
from pyexpat import model
import random
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from Resource.admin import PointOfConsumingAdmin
from Resource.models import Resource, Need, PointOfConsuming
from main.models import Volonter


class MainView(TemplateView):
    template_name = 'list_resource.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context.update({
            'Resource': Resource.objects.all(),
            'Need':Need.objects.all(),
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
#///////////////////////////////$NEED$//////////////////////////////////////////////////////////////////////////////////
class NeedListView(ListView):
    template_name = 'list_need.html'
    model = Need
    context_object_name = 'Need'

class NeedDetailView(DetailView):
    template_name = 'view_need.html'
    model = Need
    context_object_name = 'Need'

class NeedCreateView(CreateView):
    template_name = 'create_need.html'
    model = Need
    context_object_name = 'Need'
    fields = ('id_resource', 'number_of_resource', 'priority','perfomance',)
    success_url = reverse_lazy('create_need')
#/////////////////////////////////////$PointOfConsuming$////////////////////////////////////////////////////////////////////

class MainView(TemplateView):
    template_name = 'list_pointofconsuming.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context.update({
            'PointOfConsuming':PointOfConsuming.objects.all(),
        })
        return context

class PointOfConsumingListView(ListView):
    template_name = 'list_pointofconsuming.html'
    model =  PointOfConsuming
    context_object_name = 'PointOfConsuming'

class PointOfConsumingDetailView(DetailView):
    template_name = 'view_pointofconsuming.html'
    model = PointOfConsuming
    context_object_name = 'PointOfConsuming'

class PointOfConsumingCreateView(CreateView):
    template_name = 'create_pointofconsuming.html'
    model = PointOfConsuming
    context_object_name = 'PointOfConsuming'
    fields = ('id_geography_point','fio','telephone',)
    success_url = reverse_lazy('create_pointofconsuming')

class CreateVolontersView(TemplateView):
    def get(self, request, *args, **kwargs):
        print 'Fill Volonters:'
        surnames = [u'Трэк', u'Троев', u'Атеистов', u'Трюкови', u'Спайдэр', u'Виннов']
        names = [u'Вася', u'Акакий', u'Лео', u'Адольф', u'Иосиф', u'Дима', u'Игорь', u'Антон', u'Жора', u'Вася', u'Трион', u'Енот',]
        operators = [u'093', u'050', u'098', u'066', u'099']
        oblast = [u'Вінницька область',
                   u'Волинська область',
                   u'Дніпропетровська область',
                   u'Донецька область',
                   u'Закарпатська область',
                   u'Запорізька область',
                   u'Івано-Франківська область',
                   u'Київська область',
                   u'Кіровоградська область',
                   u'Луганська область',
                   u'Львівська область',
                   u'Миколаївська область',
                   u'Одеська область',
                   u'Полтавська область',
                   u'Рівненська область',
                   u'Сумська область',
                   u'Тернопільська область',
                   u'Харківська область',
                   u'Херсонська область',
                   u'Хмельницька область',
                   u'Черкаська область',
                   u'Чернігівська область',
                   u'Чернівецька область',
                   u'Автономна Республіка Крим']
        for i in range(20):
            telephone = u'+38' + random.choice(operators) + unicode(random.randint(1000000, 9999999))
            fio = random.choice(surnames) + u' ' + random.choice(names)
            address = random.choice(oblast)
            Volonter.objects.create(
                fio=fio,
                address=address,
                telephone=telephone,
                gender=u'М',
            )
            print fio, telephone
        return HttpResponse('ok')