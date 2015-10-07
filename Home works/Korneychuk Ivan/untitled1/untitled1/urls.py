from django.conf.urls import include, url
from django.contrib import admin
from main.views import MainView, VolonterListView, VolonterDetailView, VolonterCreateView, VolonterUpdateView, \
    DirectionListView, DirectionMainView, DirectionDetailView, DirectionCreateView, DirectionUpdateView, \
    TransportListView, TransportDetailView, GPointListView, GPointDetailView, OrderListView, OrderDetailView, \
    NeedListView, NeedDetailView

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

    url(r'transport/', TransportListView.as_view(), name='list_transport'),
    url(r'transport/(?P<pk>\d+)/$', TransportDetailView.as_view(), name='view_transport'),

    url(r'gpoint/', GPointListView.as_view(), name='list_geographyPoint'),
    url(r'gpoint/(?P<pk>\d+)/$', GPointDetailView.as_view(), name='view_geography'),

    url(r'order/', OrderListView.as_view(), name='list_order'),
    url(r'order/(?P<pk>\d+)/$', OrderDetailView.as_view(), name='view_order'),

    url(r'needs/', NeedListView.as_view(), name='list_need'),
    url(r'needs/(?P<pk>\d+)/$', NeedDetailView.as_view(), name='view_need'),

]
