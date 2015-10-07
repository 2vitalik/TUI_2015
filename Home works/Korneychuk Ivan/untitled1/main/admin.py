from django.contrib import admin
from django.core.urlresolvers import reverse
from main.models import Volonter, Skill, KindOfWork, Direction, KindOfTransport, Transport, Employment, GeographyPoint, \
    Order, Need


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
        'updated_at',
        'created_at',
    )
    def kind(self, obj):
        url = reverse('admin:main_kindofwork_change', args = [obj.kind.pk])
        return "Kind: <b><a href = '%s'>%s</a></b>" % (url, obj.kind.name)

class KindOfWorkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'complexity',
    )

class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'importance', )
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class KindOfTransportAdmin(admin.ModelAdmin):
    list_display = ('pk','name', 'volume', 'speed', 'expensesOfFuel', 'passability', )

class TransportAdmin(admin.ModelAdmin):
    list_display = ('pk','kindOfTransport','carsNumber',)

class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('transport','dateOfStarting','dateOfFinish','busy',)

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('pk','name','unitOfMesure',)

class StockAdmin(admin.ModelAdmin):
    list_display = ('pk','resource', 'geographyPoint', 'number',)

class GeographyPointAdmin(admin.ModelAdmin):
    list_display = ('pk','x','y','address',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk','geographyPoint','dateOfStarting','dateOfFinish','priority',)

class NeedAdmin(admin.ModelAdmin):
    list_display = ('pk','resource','order','countOfResource','priority','perfomance',)



admin.site.register(Need, NeedAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(GeographyPoint, GeographyPointAdmin)
admin.site.register(Employment, EmploymentAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(KindOfTransport, KindOfTransportAdmin)
admin.site.register(Direction, DirectionAdmin)
admin.site.register(Volonter, VolonterAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(KindOfWork, KindOfWorkAdmin)

