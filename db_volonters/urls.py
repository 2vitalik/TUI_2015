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
from django.contrib.auth.views import login, logout
from main.views import MainView, VolonterListView, VolonterDetailView, VolonterCreateView, VolonterGrafikView, \
    CreateVolontersView, ResourceGrafikView, CreateNeedsView, CreatePointOfConsumingView,FinishedView, \
    ResourceListView, DeleteCandidateVolonterView, ActivateCandidateVolonterView,MoneyView, GraphView, \
    CreateOrderView, NeedListView, NeedCreateView, MapView, AboutView, AviceView, RoatView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', MainView.as_view()),
    url(r'^$', MainView.as_view(), name='home'),

    url(r'^accounts/profile/$', MainView.as_view(), name='home'),

    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),

    url(r'^Volonter/$',VolonterListView.as_view(), name='list_volonter'),
    url(r'^Volonter/(?P<pk>\d+)/$',VolonterDetailView.as_view(), name='view_volonter'),
    url(r'^Volonter/add/',VolonterCreateView.as_view(), name='create_volonter'),

    url(r'^order/add/$',CreateOrderView.as_view(), name='create_order'),

    url(r'^advice/$',AviceView.as_view(), name='advice'),
    url(r'^map/$',MapView.as_view(), name='map_stores'),
    # url(r'^roat/$',RoatView.as_view(), name='roat'),
    url(r'^roat/(?P<pk>\d+)/$',RoatView.as_view(), name='roat'),
    url(r'^about/$',AboutView.as_view(), name='about'),

    url(r'^need/$',NeedListView.as_view(), name='list_need'),
    url(r'^need/add/$',NeedCreateView.as_view(), name='create_need'),

    # url(r'^Volonter/(?P<pk>\d+)/edit/',VolonterUpdateView.as_view(), name='update_volonter'),

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
    url(r'^resource/grafik/(?P<pk>\d+)$',ResourceGrafikView.as_view(),name = 'grafik_resource'),

    url(r'^resource/$',
        ResourceListView.as_view(),
        name='list_resource'),
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

    url(r'^actions/finished/(?P<resource_order_id>\d+)/',
        FinishedView.as_view(),
        name='finished'),
    url(r'^test/create_volonters',CreateVolontersView.as_view()),
    url(r'^test/create_needs', CreateNeedsView.as_view()),
    url(r'^test/create_pointofconsuming', CreatePointOfConsumingView.as_view()),
    url(r'response/$',MoneyView.as_view()),
    url(r'graph/$', GraphView.as_view()),
    url(r'^test/create_pointofconsuming', CreatePointOfConsumingView.as_view()),
    url(r'^actions/delete/(?P<volonter_id>\d+)/', DeleteCandidateVolonterView.as_view(), name='delete'),
    url(r'^actions/add/(?P<volonter_id>\d+)',ActivateCandidateVolonterView.as_view(), name='activate'),
    # url(r'^action/map', LeliksView.as_view(), name='leliksview')
    # url(r'actions/revertways/', RevertWayView.as_view()),
 ]
