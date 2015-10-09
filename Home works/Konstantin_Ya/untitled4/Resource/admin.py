from django.contrib import admin

# Register your models here
from Resource.models import Resource, Need


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
        'number_of_resource',
        'priority',
        'perfomance',
    )

admin.site.register(Resource, ResourceAdmin)
admin.site.register(Need, NeedAdmin)