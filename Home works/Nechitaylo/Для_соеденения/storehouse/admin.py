from django.contrib import admin
from storehouse.models import StoreHouse


class StoreHouseAdmin(admin.ModelAdmin):
    list_display = (
        'X',
        'Y',
        'V',
        'Adress',
    )
# Register your models here.

admin.site.register(StoreHouse)