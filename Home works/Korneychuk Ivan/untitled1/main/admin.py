from django.contrib import admin
from django.core.urlresolvers import reverse
from main.models import Volonter, Skill, KindOfWork, Direction


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

admin.site.register(Direction, DirectionAdmin)
admin.site.register(Volonter, VolonterAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(KindOfWork, KindOfWorkAdmin)

