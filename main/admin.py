from django.contrib import admin
from django.core.urlresolvers import reverse
from main.models import Volonter, Skill, KindOfWork, MakingAWay, Route, Way, GeographyPoint, Trip, Employment, Transport, KindOfTransport, ShippingDetalization, Shipping, Supply, Stock


class VolonterAdmin(admin.ModelAdmin):
    list_display = (
        'fio',
        'birthday',
        'address',
        'telephone',
        'gender',
        'conviction',
    )
    search_fields = ('fio', )
    list_filter = ('gender', )
    # ordering = ('pk',)


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'volonter',
        'kind',
        'proficiency',
    )
    def kind(self, obj):
        url = reverse('admin:main_kindofwork_change', args = [obj.kind.pk])
        return "Kind: <b><a href = '%s'>%s</a></b>" % (url, obj.kind.name)


class KindOfWorkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'complexity',
    )


class StockAdmin(admin.ModelAdmin):
    list_display = ('pk','storeHouseId','resource','amount','weight',)


class SupplyAdmin(admin.ModelAdmin):
    list_display = ('pk','volonter','stock','amount','dateReal','dateRecomended',)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'volonter','dateRecomended',)
class ShippingDetalizationAdmin(admin.ModelAdmin):
    list_display = ('pk','amount','shipping','stock',)
class KindOfTransportAdmin(admin.ModelAdmin):
    list_display = ('pk','name','kind','volume','speed','expenseOfFuel','passability','load')
    list_filter = ('kind',)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('pk','kindOfTransport','number')
    list_filter = ('kindOfTransport',)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'transport', 'dateStart', 'dateFinish',)
class TripAdmin(admin.ModelAdmin):
    list_display = ('pk', 'transport',  'shipping', 'dateDeparture', 'perfomance',)
class GeographyPointAdmin(admin.ModelAdmin):
    list_display = ('pk','x','y','address',)
class WayAdmin(admin.ModelAdmin):
    list_display = ('gpointFrom','gpointTo','s','danger','passability','zagruzhenost',)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('pk','storehouse','pointOfConsuming','gpointFrom','gpointTo','name',)
class MakingAWayAdmin(admin.ModelAdmin):
    list_display = ('pk','way','route','sequence',)


admin.site.register(MakingAWay, MakingAWayAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Way, WayAdmin)
admin.site.register(GeographyPoint, GeographyPointAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(Employment, EmploymentAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(KindOfTransport, KindOfTransportAdmin)
admin.site.register(ShippingDetalization, ShippingDetalizationAdmin)
admin.site.register(Shipping,ShippingAdmin)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Volonter, VolonterAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(KindOfWork, KindOfWorkAdmin)

