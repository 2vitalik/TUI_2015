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
from main.views import MainView, VolonterListView, VolonterDetailView, VolonterCreateView, VolonterUpdateView, VolonterGrafikView, \
    CreateVolontersView, ResourceGrafikView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', MainView.as_view()),
    url(r'^$', MainView.as_view()),

    url(r'^Volonter/$',VolonterListView.as_view(), name='list_volonter'),
    url(r'^Volonter/(?P<pk>\d+)/$',VolonterDetailView.as_view(), name='view_volonter'),
    url(r'^Volonter/add/',VolonterCreateView.as_view(), name='create_volonter'),
    url(r'^Volonter/(?P<pk>\d+)/edit/',VolonterUpdateView.as_view(), name='update_volonter'),

    # url(r'^StoreHouse/$',StoreHouseListView.as_view(), name= 'list_StoreHouse'),
    # url(r'^StoreHouse/(?P<pk>\d+)/$', StoreHouseDetailView.as_view(), name='view_StoreHouse' ),
    # url(r'^StoreHouse/add/$', StoreHouseCreateView.as_view(), name='create_StoreHouse' ),
    # url(r'^StoreHouse/(?P<pk>\d+)/edit/', StoreHouseUpdateView.as_view(), name='update_StoreHouse' ),
    #
    # url(r'kwork/', KindOfWorkListView.as_view(), name='list_kindofwork'),
    # url(r'kwork/(?P<pk>\d+)/$', KindOfWorkDetailView.as_view(), name='view_kindofwork'),
    #
    # url(r'skills/', SkillListView.as_view(), name='list_skill'),
    # url(r'skill/(?P<pk>\d+)/$', SkillDetailView.as_view(), name='view_skill'),
    #
    # url(r'transport/', TransportListView.as_view(), name='list_transport'),
    # url(r'transport/(?P<pk>\d+)/$', TransportDetailView.as_view(), name='view_transport'),
    #grafik_recourse
    url(r'^volonter/grafik/$',VolonterGrafikView.as_view(),name = 'grafik_volonter'),

     url(r'^resource/grafik/$',ResourceGrafikView.as_view(),name = 'grafik_resource'),

    # url(r'^Resource/$',
    #     ResourceListView.as_view(),
    #     name='list_resource'),
    # url(r'^Resource/(?P<pk>\d+)/$',
    #     ResourceDetailView.as_view(),
    #     name = 'view_resource'),
    # url(r'^Resource/add/$',
    #     ResourceCreateView.as_view(),
    #     name = 'create_resource'),
    #
    # url(r'^Need/$',
    #     NeedListView.as_view(),
    #     name = 'list_need'),
    # url(r'^Need/(?P<pk>\d+)/$',
    #     NeedDetailView.as_view(),
    #     name = 'view_need'),
    # url(r'^Need/add/$',
    #     NeedCreateView.as_view(),
    #     name = 'create_need'),
    #
    # url(r'^PointOfConsuming/$',
    #     PointOfConsumingListView.as_view(),
    #     name = 'list_pointofconsuming'),
    # url(r'^PointOfConsuming/(?P<pk>\d+)/$',
    #     PointOfConsumingDetailView.as_view(),
    #     name = 'view_pointofconsuming'),
    # url(r'^PointOfConsuming/add/$',
    #     PointOfConsumingCreateView.as_view(),
    #     name = 'create_pointofconsuming'),


    url(r'^test/create_volonters$',
        CreateVolontersView.as_view()),
]
