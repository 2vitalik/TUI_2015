# coding: utf-8
from audioop import reverse
from django.contrib import admin
from django.core.urlresolvers import reverse, reverse_lazy
from main.models import Volonter, GeographyPoint, Stock, \
    Resource, \
    PointOfConsuming, \
    Need, \
    CategoryResource, \
    ResourceOrder, \
    StoreHouse, \
    Order, Potential, Perfomance, Delivery, DeliveryDetalization, Shipping, ShippingDetalization, KindOfTransport, \
    Transport, Employment, Trip, Way, Roat, MakingRoat

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
    list_filter = ('gender', )
    def activeted(self, obj):
        img = ''
        text = ''
        if obj.activeted:
            img = u'<img src="/static/admin/img/icon-yes.gif" alt="Активований">'
            text = u'Видалити'
            url = reverse('DeleteCandidateVolonterView', args=[obj.pk])
        else:
            img = u'<img src="/static/admin/img/icon-no.gif" alt="Не активований">'
            text = u'Активувати'
            url = reverse('ActivateCandidateVolonterView', args=[obj.pk])
        return "%s <a href='%s'>%s</a>" % (img, url, text)
    activeted.allow_tags = True
    activeted.admin_order_field = 'activeted'
    activeted.short_description = 'Activeted'

class StockAdmin(admin.ModelAdmin):
    list_display = ('storeHouseId','resource','amount',)

class GeographyPointAdmin(admin.ModelAdmin):
    list_display = ('x','y','address',)

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
    list_display = (
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
    list_display = ('point_consuming', 'date_order','name',)

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
    list_display = ('point_from','point_to','roat_length','danger','passability','load',)

class RoatAdmin(admin.ModelAdmin):
    list_display = ('name','storehouse','point_consuming',)

class MakingARoatAdmin(admin.ModelAdmin):
    list_display = ('roat','way',)








admin.site.register(MakingRoat, MakingARoatAdmin)
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


