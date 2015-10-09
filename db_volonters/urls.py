"""db_volonters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from main.views import MainView, VolonterListView, VolonterDetailView, \
    VolonterCreateView, VolonterUpdateView, \
    DirectionListView, DirectionMainView, DirectionDetailView, \
    DirectionCreateView, DirectionUpdateView
from storehouse.views import StoreHouseListView, StoreHouseDetailView, StoreHouseUpdateView, \
    StoreHouseCreateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', MainView.as_view()),

    url(r'^volonters/',VolonterListView.as_view(), name='list_volonters'),
    url(r'^volonter/(?P<pk>\d+)/$',VolonterDetailView.as_view(), name='view_volonter'),
    url(r'^volonter/add/',VolonterCreateView.as_view(), name='create_volonter'),
    url(r'^volonter/(?P<pk>\d+)/edit/',VolonterUpdateView.as_view(), name='update_volonter'),

    url(r'directions/', DirectionListView.as_view(), name = 'list_directions'),
    url(r'direction/(?P<pk>\d+)/$', DirectionDetailView.as_view(), name = 'view_directions'),
    url(r'^direction/add/',DirectionCreateView.as_view(), name='create_direction'),
    url(r'^direction/(?P<pk>\d+)/edit/',DirectionUpdateView.as_view(), name='update_directions'),


    url(r'^StoreHouse/$',StoreHouseListView.as_view(), name= 'list_StoreHouse'),
    url(r'^StoreHouse/(?P<pk>\d+)/$', StoreHouseDetailView.as_view(), name='view_StoreHouse' ),
    url(r'^StoreHouse/add/$', StoreHouseCreateView.as_view(), name='create_StoreHouse' ),
    url(r'^StoreHouse/(?P<pk>\d+)/edit/', StoreHouseUpdateView.as_view(), name='update_StoreHouse' ),
]
