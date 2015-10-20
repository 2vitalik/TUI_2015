from django.contrib import admin
from django.core.urlresolvers import reverse
from main.models import Volonter, GeographyPoint, Stock, \
    Resource, \
    PointOfConsuming, \
    Need, \
    CategoryResource  #Skill, KindOfWork, MakingAWay, Route, Way,  Trip, Employment, Transport, KindOfTransport, ShippingDetalization, Shipping, Supply
# class SkillAdmin(admin.ModelAdmin):
#     list_display = (
#         'pk',
#         'volonter',
#         'kind',
#         'proficiency',
#     )
#     def kind(self, obj):
#         url = reverse('admin:main_kindofwork_change', args = [obj.kind.pk])
#         return "Kind: <b><a href = '%s'>%s</a></b>" % (url, obj.kind.name)

# class KindOfWorkAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'complexity',
#     )
# class SupplyAdmin(admin.ModelAdmin):
#     list_display = ('pk','volonter','stock','amount','dateReal','dateRecomended',)
# class ShippingAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'volonter','dateRecomended',)
# class ShippingDetalizationAdmin(admin.ModelAdmin):
#     list_display = ('pk','amount','shipping','stock',)
# class KindOfTransportAdmin(admin.ModelAdmin):
#     list_display = ('pk','name','kind','volume','speed','expenseOfFuel','passability','load')
#     list_filter = ('kind',)
# class TransportAdmin(admin.ModelAdmin):
#     list_display = ('pk','kindOfTransport','number')
#     list_filter = ('kindOfTransport',)
# class EmploymentAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'transport', 'dateStart', 'dateFinish',)
# class TripAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'transport',  'shipping', 'dateDeparture', 'perfomance',)
# class WayAdmin(admin.ModelAdmin):
#     list_display = ('gpointFrom','gpointTo','s','danger','passability','zagruzhenost',)
# class RouteAdmin(admin.ModelAdmin):
#     list_display = ('pk','storehouse','pointOfConsuming','gpointFrom','gpointTo','name',)
# class MakingAWayAdmin(admin.ModelAdmin):
#     list_display = ('pk','way','route','sequence',)


class StockAdmin(admin.ModelAdmin):
    list_display = ('storeHouseId','resource','amount',)
class GeographyPointAdmin(admin.ModelAdmin):
    list_display = ('x','y','address',)
class VolonterAdmin(admin.ModelAdmin):
    list_display = (
        'fio',
        'birthday',
        'address',
        'telephone',
        'gender',
        'categories_field',
            )
    search_fields = ('fio', )
    list_filter = ('gender', )
    filter_horizontal = ('categories', )
    # ordering = ('pk',)

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



class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category_resource', 'name', 'unit_of_mesure', 'volume_of_one_unit', 'price_one_unit',
    )
class PointOfConsumingAdmin(admin.ModelAdmin):
    list_display = ('geography_point','address','fio','telephone',)
class NeedAdmin(admin.ModelAdmin):
    list_display = ('point_consuming','resources','amount',)

    def resources(self, obj):
        return '...'
class CategoryResourceAdmin(admin.ModelAdmin):
    list_display = ('category',)


# admin.site.register(MakingAWay, MakingAWayAdmin)
# admin.site.register(Route, RouteAdmin)
# admin.site.register(Way, WayAdmin)
admin.site.register(Need, NeedAdmin)
admin.site.register(PointOfConsuming, PointOfConsumingAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(CategoryResource, CategoryResourceAdmin)
admin.site.register(GeographyPoint, GeographyPointAdmin)
# admin.site.register(Trip, TripAdmin)
# admin.site.register(Employment, EmploymentAdmin)
# admin.site.register(Transport, TransportAdmin)
# admin.site.register(KindOfTransport, KindOfTransportAdmin)
# admin.site.register(ShippingDetalization, ShippingDetalizationAdmin)
# admin.site.register(Shipping,ShippingAdmin)
# admin.site.register(Supply, SupplyAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Volonter, VolonterAdmin)
# admin.site.register(Skill, SkillAdmin)
# admin.site.register(KindOfWork, KindOfWorkAdmin)

