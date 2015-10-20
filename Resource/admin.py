# from sqlite3 import adapt
# from django.conf.app_template import admin
# from django.contrib import admin
#
# # Register your models here
# from Resource.models import Resource, Need, PointOfConsuming, Order
#
#
# class ResourceAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'description',
#     )
#     # fieldsets = (
#     #     (None, {'fields':
#     #                 ('name',
#     #                  'description',
#     #                  )
#     #             }),
#     # )
#
# class NeedAdmin(admin.ModelAdmin):
#     list_display = (
#         'resource',
#         'number_of_resource',
#         'priority',
#         'perfomance',
#     )
# class PointOfConsumingAdmin(admin.ModelAdmin):
#     list_display = (
#         'geography_point',
#         'fio',
#         'telephone',
#     )
# class OrderAdmin(admin.ModelAdmin):
#     list_display = (
#         'geography_point',
#         'date_of_starting',
#         'date_of_finish',
#         'priority',
#     )
# admin.site.register(Resource, ResourceAdmin)
# admin.site.register(Need, NeedAdmin)
# admin.site.register(PointOfConsuming,PointOfConsumingAdmin)
# admin.site.register(Order,OrderAdmin)