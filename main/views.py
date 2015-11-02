# coding: utf-8
from datetime import datetime, timedelta
import random
import urllib2
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView, TemplateView, RedirectView, View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from main.algorithms import create_stock, create_graf_chip, create_graf_danger, create_graf_time, \
    general_algo
from main.models import Volonter, Resource, Need, GeographyPoint, StoreHouse, PointOfConsuming, Order, ResourceOrder, \
    CategoryResource, Stock, Potential, Roat, Way, Transport
from django.core.mail import send_mail
import hashlib


class MainView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context.update({
            'Volonter': Volonter.objects.filter(activeted=False),
        })
        return context


class VolonterListView(ListView):
    template_name = 'list_volonter.html'
    model = Volonter
    context_object_name = 'Volonter'

    def get_context_data(self, **kwargs):
        context = super(VolonterListView, self).get_context_data(**kwargs)
        context.update({
            'Volonter':Volonter.objects.filter(activeted=True),
        })
        return context


class MapView(ListView):
    template_name = 'map.html'
    model = StoreHouse
    context_object_name = 'StoreHouse'

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context.update({
            'store_houses': StoreHouse.objects.all(),
            'point_of_consumings': PointOfConsuming.objects.all(),
            # todo: point_ccnsuming
        })
        return context


class RoatView(TemplateView):
    template_name = 'roat.html'

    def get_context_data(self, **kwargs):
        context = super(RoatView, self).get_context_data(**kwargs)
        # roat = Roat.objects.all()

        roat = Roat.objects.get(pk=self.kwargs.get('pk'))
        ways = roat.wasys.all()
        # for roat1 in roat:
        #     ways = roat1.wasys

        context.update({
            'roat': roat,
            'ways': ways,
        })

        return context


class AviceView(TemplateView):
    template_name = 'advice.html'
    # fields = ('store_house', 'point_of_consuming', 'type',)
    # success_url = reverse_lazy('#')
    def get_context_data(self, **kwargs):
        context = super(AviceView, self).get_context_data(**kwargs)
        store_house = StoreHouse.objects.all()
        point_of_consuming = PointOfConsuming.objects.all()
        context.update({
            'store_houses':store_house,
            'point_of_consumings': point_of_consuming,
        })
        return context


class AboutView(ListView):
    template_name = 'about.html'
    model = Volonter
    context_object_name = 'Volonter'


class VolonterDetailView(DetailView):
    template_name = 'view_volonter.html'
    model = Volonter
    context_object_name = 'Volonter'

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(VolonterDetailView, self).dispatch(request, *args,**kwargs)


class VolonterCreateView(CreateView):
    template_name = 'create_volonter.html'
    model = Volonter
    fields = ('fio', 'address', 'birthday',
              'telephone', 'gender','categories',)
    success_url = reverse_lazy('list_volonter')

    def get_context_data(self, **kwargs):
        context = super(VolonterCreateView, self).get_context_data(**kwargs)
        volonters = Volonter.objects.all()
        categories = CategoryResource.objects.all()
        data = []
        for category in categories:
            data.append({
                'name': category.category,
                'number': category.id,
            })
        context.update({
            'data': data,
            'Volonter': volonters,
        })
        return context
# class MapView():
#     pass

# class VolonterUpdateView(UpdateView):
#     template_name = 'update_volonter.html'
#     model = Volonter
#     context_object_name = 'Volonter'
#     fields = ('fio', 'address','telephone', 'gender')

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

        ####################################
        # data = list()
        # resource = Resource.objects.get(pk=self.kwargs.get('pk'))
        # store_houses = StoreHouse.objects.all()
        # for store_house in store_houses:
        #     stocks = Stock.objects.filter(store_house=store_house, resource=resource)
        #     # total_amount = 0
        #     # for stock in stocks:
        #     #     total_amount += stock.amount
        #     total_amount = sum([stock.amount for stock in stocks])
        #     data.append({
        #         'store_house': store_house,
        #         'total_amount': total_amount,
        #     })
        ####################################

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

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResourceGrafikView, self).dispatch(request, *args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(ResourceGrafikView, self).get_context_data(**kwargs)
        data = list()

        resource = Resource.objects.get(pk=self.kwargs.get('pk'))
        rescol = Resource.objects.all()
        store_houses = StoreHouse.objects.all()
        for store_house in store_houses:
            stocks = Stock.objects.filter(store_house = store_house, resource=resource)
            total_amount = 0
            for stock in stocks:
                total_amount += stock.amount

            # total_amount = sum([stock.amount for stock in stocks])
            data.append({
                'store_house': store_house,
                'total_amount': total_amount,
            })
        context.update({
            'data': data,
            'res': rescol,
            'select_res': resource,
        })
        return context


class CreateVolontersView(TemplateView):
    def get(self, request, *args, **kwargs):
        print 'Fill Volonters:'
        cat = CategoryResource.objects.all()
        surnames = [u'Трэк', u'Троев', u'Атеистов', u'Трюкови', u'Спайдэр', u'Виннов']
        names = [u'Вася', u'Иосиф', u'Дима', u'Игорь', u'Антон', u'Жора', u'Вася', u'Трион',]
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
        all_categories = list(CategoryResource.objects.all())
        for i in range(20):
            telephone = u'+38' + random.choice(operators) + unicode(random.randint(1000000, 9999999))
            fio = random.choice(surnames) + u' ' + random.choice(names)
            address = random.choice(oblast)

            volonter = Volonter.objects.create(
                fio=fio,
                address=address,
                telephone=telephone,
                gender=u'М',
            )
            for i in range(random.randint(1, 2)):
                volonter.categories.add(random.choice(all_categories))
            print fio, telephone
        return HttpResponse('ok')


class CreateNeedsView(TemplateView):
    def get(self, request, *args, **kwargs):
        point_consuming1 = PointOfConsuming.objects.all()
        resource1 = list(Resource.objects.all())
        amount1 = [5,10,15,20,25,30,35,40,45,50,]

        for i in range(10):
            point_consuming2 = random.choice(point_consuming1)
            resource2 = random.choice(resource1)
            amount2 = random.choice(amount1)
            Need.objects.create(
                point_consuming=point_consuming2,
                resource=resource2,
                amount=amount2,
            )
        return HttpResponse('ok')


class CreatePointOfConsumingView(TemplateView):
    def get(self, request, *args, **kwargs):
        ge_points = GeographyPoint.objects.all()
        storehouses = StoreHouse.objects.all()
        surnames = [u'Трэк', u'Троев', u'Атеистов', u'Трюкови', u'Спайдэр', u'Виннов']
        names = [u'Вася', u'Акакий', u'Лео', u'Адольф', u'Иосиф', u'Дима', u'Игорь', u'Антон', u'Жора', u'Вася', u'Трион', u'Енот',]
        operators = [u'093', u'050', u'098', u'066', u'099']
        point_cons = []
        for point in ge_points:
            is_store = False
            is_point_con = False
            try:
                store = point.storehouse
                is_store = True
            except ObjectDoesNotExist:
                pass
            try:
                point_con = point.pointofconsuming
                is_point_con = True
            except ObjectDoesNotExist:
                pass

            if not is_store and not is_point_con:
                point_cons.append(point)

        # order = Order()
        # for need in order.need_set.all():
        #     pass

        # p = GeographyPoint()
        # p.storehouse
        # p.pointofconsuming

        for i in range(10):
            print i
            telephone1 = u'+38' + random.choice(operators) + unicode(random.randint(1000000, 9999999))
            fio1 = random.choice(surnames) + u' ' + random.choice(names)
            point_cons1 = random.choice(list(point_cons))
            point_cons.remove(point_cons1)
            PointOfConsuming.objects.create(
                geography_point = point_cons1,
                fio = fio1,
                telephone = telephone1,
            )
        return HttpResponse('ok')


class FinishedView(RedirectView):
    permanent = False
    url = reverse_lazy('admin:main_resourceorder_changelist')

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(FinishedView, self).dispatch(request, *args,**kwargs)

    def get(self, request, *args, **kwargs):
        resource_order_id = kwargs.get('resource_order_id')
        resource_order = ResourceOrder.objects.get(pk=resource_order_id)
        resource_order.finished = not resource_order.finished
        resource_order.save()
        create_stock(resource_order)
        return super(FinishedView, self).get(request, *args,**kwargs)


class ResourceListView(ListView):
    template_name = 'list_resource.html'
    model = Resource
    context_object_name = 'Resource'


class MoneyView(View):
    def get(self, request, *args, **kwargs):
        data = """<oper>cmt</oper>
<wait>0</wait>
<test>0</test>
<payment id="">
<prop name="sd" value="%s" />
<prop name="ed" value="%s" />
<prop name="card" value="5168755932903558" />
</payment>""" % (datetime.now().strftime("%d.%m.%Y"),(datetime.now() - timedelta(days=100)).strftime("%d.%m.%Y"))
        sign = hashlib.sha1(hashlib.md5(data +'UB3JFMI30N4GY81eXLNShe45I6sv3b0T').hexdigest()).hexdigest()
        ddd = """<?xml version="1.0" encoding="UTF-8"?>
<request version="1.0">
<merchant>
<id>112956</id>
<signature>%s</signature>
</merchant>
<data>
%s
</data>
</request>""" % (sign, data)
        print ddd
        r = urllib2.Request("https://api.privatbank.ua/p24api/rest_fiz", data=ddd,
                         headers={'Content-Type': 'application/xml'})
        u = urllib2.urlopen(r)
        response = u.read()
        return HttpResponse(response)


class GraphView(View):
    def get(self, request, *args, **kwargs):
        # create_graf()
        return HttpResponse('Мы удалили функцию create_graf() отсюда :)')

class FirstAlgoView(View):
    def get(self, request, *args, **kwargs):
       pass

class CreatePotentialView(TemplateView):
    def get(self, request, *args, **kwargs):
        volonter1 = Volonter.objects.all()
        category1 = CategoryResource.objects.all()
        period1 = [u'Кожного разу',u'Кожної неділі',u'Кожного місяця']

        for i in range(30):
            volonter = random.choice(volonter1)
            category = random.choice(category1)
            period = random.choice(period1)
            Potential.objects.create(

            )


class DeleteCandidateVolonterView(RedirectView):
    permanent = False
    url = reverse_lazy('admin:main_volonter_changelist')

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteCandidateVolonterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        volonter_id = kwargs.get('volonter_id')
        volonter = Volonter.objects.get(pk=volonter_id)
        volonter.delete()
        return super(DeleteCandidateVolonterView, self).get(request, *args, **kwargs)


class ActivateCandidateVolonterView(RedirectView):
    permanent = False
    url = reverse_lazy('admin:main_volonter_changelist')

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ActivateCandidateVolonterView, self).dispatch(request, *args,**kwargs)

    def get(self, request, *args, **kwargs):
        volonter_id = kwargs.get('volonter_id')
        volonter = Volonter.objects.get(pk=volonter_id)
        volonter.convictions = not volonter.convictions
        volonter.save()
        return super(ActivateCandidateVolonterView, self).get(request, *args, **kwargs)


class NeedListView(ListView):
    template_name = 'list_need.html'
    model = Need
    context_object_name = 'Needs'


class NeedCreateView(CreateView):
    template_name = 'create_need.html'
    model = Need
    context_object_name = 'Needs'
    fields = ('resource', 'amount','order', 'priority')
    success_url = reverse_lazy('list_need')

    def get_context_data(self, **kwargs):
        context = super(NeedCreateView, self).get_context_data(**kwargs)

        ress = Resource.objects.all()
        orders = Order.objects.all()
        context.update({
            'resurs': ress,
            'orders': orders,
        })
        return context


class CreateOrderView(TemplateView):
    template_name = 'create_order.html'

    def post(self, request, *args, **kwargs):
        order = Order.objects.create(point_consuming=request.user.point_consuming)
        for i in range(1, 20):
            if request.POST.get('amount_%d' % i):
                Need.objects.create(
                    amount=request.POST.get('amount_%d' % i),
                    resource_id=int(request.POST.get('resource_%d' % i)),
                    priority=request.POST.get('priority_%d' % i),
                    date_recomended=request.POST.get('data_%d' % i),
                    order=order,
                )
        return redirect('home')

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateOrderView, self).dispatch(request, *args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateOrderView, self).get_context_data(**kwargs)

        ress = Resource.objects.all()
        orders = Order.objects.all()
        context.update({
            'resurs': ress,
            'orders': orders,
            'numbers': range(1, 20),
        })
        return context


class GeneralAlgoView(TemplateView):
    template_name = 'admin/general_algo.html'

    def get(self, request, *args, **kwargs):
        general_algo()
        return super(GeneralAlgoView, self).get(request, *args, **kwargs)


# class LeliksView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         pass
#         return HttpResponse('OK')
# class RevertWayView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         ways = Way.objects.all()
#         for way in ways:
#             Way.objects.create(
#                 point_from = way.point_to,
#                 point_to = way.point_from,
#                 roat_length = way.roat_length,
#                 danger = way.danger,
#                 passability = way.passability,
#                 load = way.load,
#                 yandex_or_byhand = way.yandex_or_byhand,
#             )
#         return HttpResponse('OK')


class CreateRoat(RedirectView):

    def get(self, request, *args, **kwargs):
        store_house_pri = request.POST.get('store_house')
        point_of_consuming_pri = request.POST.get('point_of_consuming')
        type = request.POST.get('type')
        best_transport = None
        best_value = 1e9
        best_pairs = None
        # store_house = StoreHouse.objects.get(pk=self.kwargs.get('store_house_pri'))
        # point_of_consuming = PointOfConsuming.objects.get(pk=self.kwargs.get('point_of_consuming_pri'))
        store_house = StoreHouse.objects.get(pk=store_house_pri)
        point_of_consuming = PointOfConsuming.objects.get(pk=point_of_consuming_pri)

        if type == '3':
            for transport in Transport.objects.all():
                a = create_graf_chip(store_house, point_of_consuming, transport)
                if a[1] < best_value:
                    best_transport = transport
                    best_value = a[1]
                    best_pairs = a[0]
        elif type == '2':

            for transport in Transport.objects.all():
                a = create_graf_danger(store_house, point_of_consuming, transport)
                if a[1] < best_value:
                    best_transport = transport
                    best_value = a[1]
                    best_pairs = a[0]
        elif type == '1':

            for transport in Transport.objects.all():
                a = create_graf_time(store_house, point_of_consuming, transport)
                if a[1] < best_value:
                    best_transport = transport
                    best_value = a[1]
                    best_pairs = a[0]

        # roat = create_roat(best_pairs,store_house,point_of_consuming,best_transport)
        # roat.storehouse_id = store_house
        # roat.point_of_consuming_id = point_of_consuming
        # roat.transport = best_transport
        # roat.transport = best_transport
        # roat.wasys.add(was.get(pk=''))
        # roat.wasys.add(1)
        # roat.storehouse_id = store_house
        # roat.point_of_consuming_id = point_of_consuming

        roat = Roat(name=store_house.geography_point.address,storehouse=store_house,transport=best_transport, point_consuming= point_of_consuming )
        roat.save()
        for pair in best_pairs:
            way = Way.objects.get(point_from_id=pair[0], point_to_id=pair[1])
            roat.wasys.add(way.pk)

        # print(roat.pk)


        # return redirect('roat', args=[roat.pk])
        return redirect('roat', roat.pk)