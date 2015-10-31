# coding: utf-8
from audioop import reverse
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from main.forms import CustomUserChangeForm, CustomUserCreationForm, CustomAdminPasswordChangeForm
from main.models import Volonter, GeographyPoint, Stock, \
    Resource, \
    PointOfConsuming, \
    Need, \
    CategoryResource, \
    ResourceOrder, \
    StoreHouse, \
    Order, Potential, Perfomance, Delivery, DeliveryDetalization, Shipping, ShippingDetalization, KindOfTransport, \
    Transport, Employment, Trip, Way, Roat, MakingRoat


class StockAdmin(admin.ModelAdmin):
    list_display = ('store_house','resource','amount',)


class GeographyPointAdmin(admin.ModelAdmin):
    list_display = ('x','y','address',)


class VolonterAdmin(admin.ModelAdmin):
    list_display = (
        'fio',
        'birthday',
        'address',
        'telephone',
        'gender',
        'activeted',
    )
    search_fields = ('fio', )
    list_filter = ('gender', 'address',
                   'categories',
                   'birthday')
    filter_horizontal = ('categories', )
    date_hierarchy = 'birthday'

    def categories_field(self, obj):
        return ', '.join([o.category for o in obj.categories.all()])
        # res = ''
        # for o in obj.categories.all():
        #     if res:
        #         res += ', '
        #     res += o.category
        # a = ['1', '2', '3']
        # print ' '.join(a)
        # b = [o + ' m' for o in a]
        # print '; '.join(b)
    categories_field.short_description = u'Категорії'
    
    def activeted(self, obj):
        img = ''
        text = ''
        if obj.activeted:
            img = u'<img src="/static/admin/img/icon-yes.gif" alt="Активований">'
            text = u'Видалити'
            url = reverse('delete', args=[obj.pk])
        else:
            img = u'<img src="/static/admin/img/icon-no.gif" alt="Не активований">'
            text = u'Активувати'
            url = reverse('activate', args=[obj.pk])
        return "%s <a href='%s'>%s</a>" % (img, url, text)
    activeted.allow_tags = True


class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category_resource','unit_of_mesure', 'volume_of_one_unit', 'price_one_unit', 'weight_one_unit',
    )


class PointOfConsumingAdmin(admin.ModelAdmin):
    list_display = ('geography_point','fio','telephone',)


class NeedAdmin(admin.ModelAdmin):
    list_display = ('resource','amount','order','priority','finished','date_recomended',)


class CategoryResourceAdmin(admin.ModelAdmin):
    list_display = ('category',)


class ResourceOrderAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'resource',
                    'amount',
                    'choise_finished',
                    'date_created',
                    'date_finished',
    )

    def choise_finished(self, obj):
        img = ''
        text = ''
        if obj.finished:
            img = '<img src="/static/admin/img/icon-yes.gif" alt="Finished">'
            text = 'finished'
            return "%s-%s" % (img,text)
        else:
            img = '<img src="/static/admin/img/icon-no.gif" alt="No_Finished">'
            text = '-add'
            url = reverse('finished', args=[obj.pk])
            return "%s <a href='%s'>%s</a>" % (img, url, text)

    choise_finished.allow_tags = True
    choise_finished.admin_order_field = 'finished'
    choise_finished.short_description = 'Finished'


class StoreHouseAdmin(admin.ModelAdmin):
    list_display = ('geography_point', 'volume','free_volume','rent')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name','needs', 'point_consuming', 'date_order',)

    def needs(self, obj):
        return ', '.join(["%s/%s" % (o.resource, o.amount) for o in obj.need_set.all()])


class PotentialAdmin(admin.ModelAdmin):
    list_display = ('volonter','category','period',)


class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('need','amount','date',)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('volonter','resource','amount','date_recomended','date_real',)


class DeliveryDetalizationAdmin(admin.ModelAdmin):
    list_display = ('shipping','storehouse','amount',)


class ShippingAdmin(admin.ModelAdmin):
    list_display = ('date_recomended',)


class ShippingDetalizationAdmin(admin.ModelAdmin):
    list_display = ('shipping','stock','amount',)


class KindOfTransportAdmin(admin.ModelAdmin):
    list_display = ('name','category','speed','expences_fuel','volume_transport','max_weight','passability',)


class TransportAdmin(admin.ModelAdmin):
    list_display = ('kind_of_transport','number')


class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('transport','date_start','date_finish',)


class TripAdmin(admin.ModelAdmin):
    list_display = ('transport','shipping','date_start','perfomance',)


class WayAdmin(admin.ModelAdmin):
    list_display = ('point_from','point_to','roat_length','danger','passability','load','yandex_or_byhand',)


class RoatAdmin(admin.ModelAdmin):
    list_display = ('name','storehouse','point_consuming','transport','on_the_map',)
    def on_the_map(self,obj):
        text = u'Подивитися на карті'
        url = reverse('leliksview')
        return "<a href='%s'>%s</a>" % (url, text)
    on_the_map.allow_tags = True
    on_the_map.admin_order_field = u'Карта'
    on_the_map.short_description = u'Карта'

class MakingARoatAdmin(admin.ModelAdmin):
    list_display = ('roat','way',)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    change_password_form = CustomAdminPasswordChangeForm







admin.site.register(MakingRoat, MakingARoatAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Roat, RoatAdmin)
admin.site.register(Way, WayAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(Employment, EmploymentAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(KindOfTransport, KindOfTransportAdmin)
admin.site.register(ShippingDetalization,  ShippingDetalizationAdmin)
admin.site.register(Shipping, ShippingAdmin)
admin.site.register(DeliveryDetalization,DeliveryDetalizationAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Perfomance, PerformanceAdmin)
admin.site.register(Potential, PotentialAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(StoreHouse, StoreHouseAdmin)
admin.site.register(ResourceOrder, ResourceOrderAdmin)
admin.site.register(Need, NeedAdmin)
admin.site.register(PointOfConsuming, PointOfConsumingAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(CategoryResource, CategoryResourceAdmin)
admin.site.register(GeographyPoint, GeographyPointAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Volonter, VolonterAdmin)
