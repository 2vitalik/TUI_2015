from django.conf.urls import include, url
from django.contrib import admin
from main.views import MainView, VolonterListView, VolonterDetailView, VolonterCreateView, VolonterUpdateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', MainView.as_view()),
    url(r'^volonters/',
        VolonterListView.as_view(),
        name='list_volonters'),
    url(r'^volonter/(?P<pk>\d+)/$',
        VolonterDetailView.as_view(),
        name='view_volonter'),
    url(r'^volonter/add/',
        VolonterCreateView.as_view(),
        name='create_volonter'),
    url(r'^volonter/(?P<pk>\d+)/edit/',
        VolonterUpdateView.as_view(),
        name='update_volonter'),
]
