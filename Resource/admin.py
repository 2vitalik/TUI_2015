from sqlite3 import adapt
from django.conf.app_template import admin
from django.contrib import admin

# Register your models here
from Resource.models import Resource, Need, PointOfConsuming, Order


class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'weight',
        'volume',
        'count',
    )
    fieldsets = (
        (None, {'fields':
                    ('name',
                     ('weight', 'volume','count'),
                     )
                }),
    )

class NeedAdmin(admin.ModelAdmin):
    list_display = (
        'id_resource',
        'number_of_resource',
        'priority',
        'perfomance',
    )
class PointOfConsumingAdmin(admin.ModelAdmin):
    list_display = (
        'id_geography_point',
        'fio',
        'telephone',
    )
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id_geography_point',
        'date_of_starting',
        'date_of_finish',
        'priority',
    )
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Need, NeedAdmin)
admin.site.register(PointOfConsuming,PointOfConsumingAdmin)
admin.site.register(Order,OrderAdmin)