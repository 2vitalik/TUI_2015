# coding: utf-8
import random
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, TemplateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from main.models import Volonter, KindOfWork, Skill, Transport


class MainView(TemplateView):
    template_name = 'list_volonter.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context.update({
            'Volonter': Volonter.objects.all(),
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
    fields = ('fio', 'address', 'birthday',
              'telephone', 'gender',)
    success_url = reverse_lazy('list_volonter')

class VolonterUpdateView(UpdateView):
    template_name = 'update_volonter.html'
    model = Volonter
    context_object_name = 'Volonter'
    fields = ('fio', 'address','telephone', 'gender')

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# class KindOfWorkMainView(TemplateView):
#     template_name = 'list_kindofwork.html'
#     def get_context_data(self, **kwargs):
#         context = super(KindOfWorkMainView, self).get_context_data()
#         context.update({'kWorks':KindOfWork.objects.all()})
#         return context
# class KindOfWorkListView(ListView):
#     template_name = 'list_kindofwork.html'
#     model = KindOfWork
#     context_object_name = 'kWork'
# class KindOfWorkDetailView(DetailView):
#     template_name = 'view_kindofwork.html'
#     model = KindOfWork
#     context_object_name = 'kWork'
# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# class SkillMainView(TemplateView):
#     template_name = 'list_skill.html'
#     def get_context_data(self, **kwargs):
#         context = super(SkillMainView, self).get_context_data()
#         context.update({'skills': Skill.objects.all()})
#         return context
# class SkillListView(ListView):
#     template_name = 'list_skill.html'
#     model = Skill
#     context_object_name = 'skills'
# class SkillDetailView(DetailView):
#     template_name = 'view_skill.html'
#     model = Skill
#     context_object_name = 'skill'
# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# class TransportMainView(TemplateView):
#     template_name = 'list_transport.html'
#     def get_context_data(self, **kwargs):
#         context = super(TransportMainView, self).get_context_data()
#         context.update({'trans': Transport.objects.all()})
#         return context
# class TransportListView(ListView):
#     template_name = 'list_transport.html'
#     model = Transport
#     context_object_name = 'trans'
# class TransportDetailView(DetailView):
#     template_name = 'view_transport.html'
#     model = Transport
#     context_object_name = 'trans'


class VolonterGrafikView(ListView):
    template_name = 'grafik_volonter.html'
    model = Volonter
    context_object_name = 'Volonter'

    def get_context_data(self, **kwargs):
        context = super(VolonterGrafikView, self).get_context_data(**kwargs)
        oblasti = [u'Вінницька область',
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
                   u'Автономна Республіка Крим',]
        data = []
        N = 1
        for oblast in oblasti:
            count = Volonter.objects.filter(address__contains=oblast).count()
            data.append({
                'name': oblast,
                'count': count,
                'val': N
            })
            N=N+1
        context.update({
            'data': data,
        })
        return context


class ResourceGrafikView(ListView):
    template_name = 'grafik_resource.html'
    model = Resource
    context_object_name = 'Resource'
    # def get_context_data(self, **kwargs):
    #     context = super(ResourceGrafikView, self).get_context_data(**kwargs)
    #     data = []
    #     context.update({
    #         'data': data,
    #     })
    #     return context


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