from django.contrib import admin
from main.models import Volonter, Skill, KindOfWork, Direction


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


class KindOfWorkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'complexity'
    )

class DirectionAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Importance', )

admin.site.register(Direction, DirectionAdmin)
admin.site.register(Volonter, VolonterAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(KindOfWork, KindOfWorkAdmin)

