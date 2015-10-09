from django.contrib import admin
from main.models import Volonter, Skill, KindOfWork, Order


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
        'about',
    )
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'kind',
        'about',
    )

admin.site.register(Volonter, VolonterAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(KindOfWork, KindOfWorkAdmin)
admin.site.register(Order, OrderAdmin)
