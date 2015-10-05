from django.conf.app_template import admin
from django.contrib import admin
from main.models import Volonter, Skill, KindOfWork, Resource, Stock

class VolonterAdmin(admin.ModelAdmin):
    list_display = (
        'fio',
        'birthday',
        'address',
        'telephone',
        'gender',
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
    # ordering = ('created_at', )
    # ordering = ['created_at']

class KindOfWorkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
class StockAdmin(admin.ModelAdmin):
    list_display = (
        'resource',
    )
admin.site.register(Volonter, VolonterAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(KindOfWork, KindOfWorkAdmin)
admin.site.register(Resource,ResourceAdmin)
admin.site.register(Stock,StockAdmin)
