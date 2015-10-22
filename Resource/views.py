# # coding: utf-8
# from httplib import HTTPResponse
# from pyexpat import model
# import random
# from django.http.response import HttpResponse
# from django.shortcuts import render
# from django.core.urlresolvers import reverse_lazy
# from django.views.generic import TemplateView, ListView, DetailView, CreateView
# from Resource.admin import PointOfConsumingAdmin
# from Resource.models import Resource, Need, PointOfConsuming
# from main.models import Volonter
#
#
# class MainView(TemplateView):
#     template_name = 'list_resource.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MainView, self).get_context_data(**kwargs)
#         context.update({
#             'Resource': Resource.objects.all(),
#             'Need':Need.objects.all(),
#         })
#         return context
#
# class ResourceListView(ListView):
#     template_name = 'list_resource.html'
#     model = Resource
#     context_object_name = 'Resource'
#
# class ResourceDetailView(DetailView):
#     template_name = 'view_resource.html'
#     model = Resource
#     context_object_name = 'Resource'
#
# class ResourceCreateView(CreateView):
#     template_name = 'create_resource.html'
#     model = Resource
#     context_object_name = 'Resource'
#     fields = ('name', 'weight', 'volume','count',)
#     success_url = reverse_lazy('create_resource')
# #///////////////////////////////$NEED$//////////////////////////////////////////////////////////////////////////////////
# class NeedListView(ListView):
#     template_name = 'list_need.html'
#     model = Need
#     context_object_name = 'Need'
#
# class NeedDetailView(DetailView):
#     template_name = 'view_need.html'
#     model = Need
#     context_object_name = 'Need'
#
# class NeedCreateView(CreateView):
#     template_name = 'create_need.html'
#     model = Need
#     context_object_name = 'Need'
#     fields = ('id_resource', 'number_of_resource', 'priority','perfomance',)
#     success_url = reverse_lazy('create_need')
# #/////////////////////////////////////$PointOfConsuming$////////////////////////////////////////////////////////////////////
#
# class MainView(TemplateView):
#     template_name = 'list_pointofconsuming.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MainView, self).get_context_data(**kwargs)
#         context.update({
#             'PointOfConsuming':PointOfConsuming.objects.all(),
#         })
#         return context
#
# class PointOfConsumingListView(ListView):
#     template_name = 'list_pointofconsuming.html'
#     model =  PointOfConsuming
#     context_object_name = 'PointOfConsuming'
#
# class PointOfConsumingDetailView(DetailView):
#     template_name = 'view_pointofconsuming.html'
#     model = PointOfConsuming
#     context_object_name = 'PointOfConsuming'
#
# class PointOfConsumingCreateView(CreateView):
#     template_name = 'create_pointofconsuming.html'
#     model = PointOfConsuming
#     context_object_name = 'PointOfConsuming'
#     fields = ('id_geography_point','fio','telephone',)
#     success_url = reverse_lazy('create_pointofconsuming')
#
# class CreateVolontersView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         print 'Fill Volonters:'
#         surnames = [u'РўСЂСЌРє', u'РўСЂРѕРµРІ', u'РђС‚РµРёСЃС‚РѕРІ', u'РўСЂСЋРєРѕРІРё', u'РЎРїР°Р№РґСЌСЂ', u'Р’РёРЅРЅРѕРІ']
#         names = [u'Р’Р°СЃСЏ', u'РђРєР°РєРёР№', u'Р›РµРѕ', u'РђРґРѕР»СЊС„', u'Р�РѕСЃРёС„', u'Р”РёРјР°', u'Р�РіРѕСЂСЊ', u'РђРЅС‚РѕРЅ', u'Р–РѕСЂР°', u'Р’Р°СЃСЏ', u'РўСЂРёРѕРЅ', u'Р•РЅРѕС‚',]
#         operators = [u'093', u'050', u'098', u'066', u'099']
#         oblast = [u'Р’С–РЅРЅРёС†СЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'Р’РѕР»РёРЅСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'Р”РЅС–РїСЂРѕРїРµС‚СЂРѕРІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'Р”РѕРЅРµС†СЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'Р—Р°РєР°СЂРїР°С‚СЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'Р—Р°РїРѕСЂС–Р·СЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'Р†РІР°РЅРѕ-Р¤СЂР°РЅРєС–РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'РљРёС—РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'РљС–СЂРѕРІРѕРіСЂР°РґСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'Р›СѓРіР°РЅСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'Р›СЊРІС–РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'РњРёРєРѕР»Р°С—РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'РћРґРµСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'РџРѕР»С‚Р°РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'Р С–РІРЅРµРЅСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'РЎСѓРјСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'РўРµСЂРЅРѕРїС–Р»СЊСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'РҐР°СЂРєС–РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'РҐРµСЂСЃРѕРЅСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'РҐРјРµР»СЊРЅРёС†СЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'Р§РµСЂРєР°СЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'Р§РµСЂРЅС–РіС–РІСЃСЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'Р§РµСЂРЅС–РІРµС†СЊРєР° РѕР±Р»Р°СЃС‚СЊ',
#                    u'РђРІС‚РѕРЅРѕРјРЅР° Р РµСЃРїСѓР±Р»С–РєР° РљСЂРёРј']
#         for i in range(20):
#             telephone = u'+38' + random.choice(operators) + unicode(random.randint(1000000, 9999999))
#             fio = random.choice(surnames) + u' ' + random.choice(names)
#             address = random.choice(oblast)
#             Volonter.objects.create(
#                 fio=fio,
#                 address=address,
#                 telephone=telephone,
#                 gender=u'Рњ',
#             )
#             print fio, telephone
#         return HttpResponse('ok')