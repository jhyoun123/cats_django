from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'add_home$', views.add_home),
    url(r'add$', views.add),
    url(r'delete/(?P<id>\d+)$', views.delete),
    url(r'edit/(?P<id>\d+)$', views.edit),
    url(r'edit_new/(?P<id>\d+)$', views.edit_info),
    url(r'show/(?P<id>\d+)$', views.show),
    url(r'like/(?P<id>\d+)$', views.like),
]