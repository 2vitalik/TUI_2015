from django.contrib import admin
from django.core.urlresolvers import reverse
from main.models import Volonter, GeographyPoint, Stock, \
    Resource, \
    PointOfConsuming, \
    Need, \
    CategoryResource, \
    ResourceOrder, \
    StoreHouse, \
    Order
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
    list_display = ('point_consuming','resource','amount',)
class CategoryResourceAdmin(admin.ModelAdmin):
    list_display = ('category',)
class ResourceOrderAdmin(admin.ModelAdmin):
    list_display = ('pk','resource','store_house','amount','finished','date_created','date_finished',)
class StoreHouseAdmin(admin.ModelAdmin):
    list_display = ('volume','rent','geography_point',)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('needs_field',)
    filter_horizontal = ('needs',)

    def needs_field(self, obj):
        return ', '.join([(o.resource, o.amount) for o in obj.needs.all()])



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


