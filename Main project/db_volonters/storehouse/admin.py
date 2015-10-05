from django.contrib import admin
from storehouse.models import StoreHouse


class StoreHouseAdmin(admin.ModelAdmin):
    list_display = (
        'X',
        'Y',
        'V',
        'Address',
    )
    search_fields = ('Adress', )

admin.site.register(StoreHouse)
