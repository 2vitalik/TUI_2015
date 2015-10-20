# coding: utf-8
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
import Resource
from main.models import Volonter



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

class VolonterGrafikView(ListView):
    template_name = 'grafik_volonter.html'
    model = Volonter
    context_object_name = 'Volonter'

    def get_context_data(self, **kwargs):
        context = super(VolonterGrafikView, self).get_context_data(**kwargs)
        oblasti = [u'Р’С–РЅРЅРёС†СЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'Р’РѕР»РёРЅСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'Р”РЅС–РїСЂРѕРїРµС‚СЂРѕРІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'Р”РѕРЅРµС†СЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'Р—Р°РєР°СЂРїР°С‚СЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'Р—Р°РїРѕСЂС–Р·СЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'Р†РІР°РЅРѕ-Р¤СЂР°РЅРєС–РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'РљРёС—РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'РљС–СЂРѕРІРѕРіСЂР°РґСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'Р›СѓРіР°РЅСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'Р›СЊРІС–РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'РњРёРєРѕР»Р°С—РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'РћРґРµСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'РџРѕР»С‚Р°РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'Р С–РІРЅРµРЅСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'РЎСѓРјСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'РўРµСЂРЅРѕРїС–Р»СЊСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'РҐР°СЂРєС–РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'РҐРµСЂСЃРѕРЅСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'РҐРјРµР»СЊРЅРёС†СЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'Р§РµСЂРєР°СЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'Р§РµСЂРЅС–РіС–РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'Р§РµСЂРЅС–РІРµС†СЊРєР° РѕР±Р»Р°СЃС‚СЊ',
                   u'РђРІС‚РѕРЅРѕРјРЅР° Р РµСЃРїСѓР±Р»С–РєР° РљСЂРёРј',]
        data = []
        for oblast in oblasti:
            count = Volonter.objects.filter(address__contains=oblast).count()
            data.append({
                'name': oblast,
                'count': count
            })
        context.update({
            'data': data,
        })
        return context
