"""untitled1 URL Configuration

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
from storehouse.views import StoreHouseListView, MainView, StoreHouseDetailView, StoreHouseUpdateView, \
    StoreHouseCreateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', MainView.as_view()),

    url(r'^StoreHouse/$',
         StoreHouseListView.as_view(),
         name= 'list_StoreHouse'),


    url(r'^StoreHouse/(?P<pk>\d+)/$',
        StoreHouseDetailView.as_view(),
        name='view_StoreHouse' ),

    url(r'^StoreHouse/add/$',
        StoreHouseCreateView.as_view(),
        name='create_StoreHouse' ),

    url(r'^StoreHouse/(?P<pk>\d+)/edit/',
        StoreHouseUpdateView.as_view(),
        name='update_StoreHouse' ),
]
