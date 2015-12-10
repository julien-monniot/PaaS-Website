from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.travel_list, name='travel_list'),
    url(r'^(?P<pk>\d+)/$', views.travel_detail, name='travel_detail'),

    url(r'^(?P<pk>\d+)/subscribe$', views.travel_subscribe, name='travel_subscribe'),
    url(r'^(?P<pk>\d+)/unsubscribe$', views.travel_unsubscribe, name='travel_unsubscribe'),
    url(r'^mytravels/$', views.my_travels, name='my_travels'),
    url(r'^mycreatedtravels/$', views.my_created_travels, name='my_created_travels'),
    url(r'^create/$', views.create_travel, name='create_travel')
)
