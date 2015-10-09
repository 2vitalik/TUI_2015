from django.conf.urls import include, url
from django.contrib import admin
from main.views import MainView, VolonterListView, VolonterDetailView, KindOfWorkListView, KindOfWorkDetailView, \
    SkillListView, SkillDetailView, TransportListView, TransportDetailView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', MainView.as_view()),

    url(r'^volonters/',VolonterListView.as_view(), name='list_volonters'),
    url(r'^volonter/(?P<pk>\d+)/$',VolonterDetailView.as_view(), name='view_volonter'),

    url(r'kwork/', KindOfWorkListView.as_view(), name='list_kindofwork'),
    url(r'kwork/(?P<pk>\d+)/$', KindOfWorkDetailView.as_view(), name='view_kindofwork'),

    url(r'skills/', SkillListView.as_view(), name='list_skill'),
    url(r'skill/(?P<pk>\d+)/$', SkillDetailView.as_view(), name='view_skill'),

    url(r'transport/', TransportListView.as_view(), name='list_transport'),
    url(r'transport/(?P<pk>\d+)/$', TransportDetailView.as_view(), name='view_transport')
]
