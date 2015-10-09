"""untitled4 URL Configuration

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
from unicodedata import name
from django.conf.urls import include, url
from django.contrib import admin
from Resource.views import MainView, ResourceListView, ResourceDetailView, ResourceCreateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', MainView.as_view()),
    url(r'^Resource/$',
        ResourceListView.as_view(),
        name='list_resource'),
    url(r'^Resource/(?P<pk>\d+)/$',
        ResourceDetailView.as_view(),
        name = 'view_resource'),
    url (r'^Resource/add/$',
         ResourceCreateView.as_view(),
         name = 'create_resource'),
]
