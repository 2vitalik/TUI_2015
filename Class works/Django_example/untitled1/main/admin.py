from django.contrib import admin
from django.core.urlresolvers import reverse
from main.models import Volonter, Skill, KindOfWork


class VolonterAdmin(admin.ModelAdmin):
    list_display = (
        'fio',
        'birthday',
        'address',
        'telephone',
        'gender',
        'change_convictions',
    )
    search_fields = ('fio', )
    list_filter = ('gender', )
    # ordering = ('pk',)

    def change_convictions(self, obj):
        img = ''
        text = ''
        if obj.convictions:
            img = '<img src="/static/admin/img/icon-no.gif" alt="Has convictions">'
            text = 'remove convictions'
        else:
            img = '<img src="/static/admin/img/icon-yes.gif" alt="Hasn\'t convictions">'
            text = 'add convictions'
        url = reverse('change_convictions', args=[obj.pk])
        return "%s <a href='%s'>%s</a>" % (img, url, text)
    change_convictions.allow_tags = True
    change_convictions.admin_order_field = 'convictions'
    change_convictions.short_description = 'Convictions'

class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'volonter',
        'kind_field',
        'updated_at',
        'created_at',
    )
    # ordering = ('created_at', )
    # ordering = ['created_at']

    def kind_field(self, obj):
        url = reverse('admin:main_kindofwork_change', args=[obj.kind.pk])
        return "Kind: <b><a href='%s'>%s</a></b>" % (url, obj.kind.name)
    kind_field.allow_tags = True
    kind_field.short_description = 'Kind of work'
    kind_field.admin_order_field = 'kind__name'


class KindOfWorkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Volonter, VolonterAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(KindOfWork, KindOfWorkAdmin)

