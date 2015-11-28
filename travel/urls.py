from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.travel_list, name='travel_list'),
    url(r'^(?P<pk>\d+)/$', views.travel_detail, name='travel_detail'),
    url(r'^create/$', views.create_travel, name='create_travel'),
)
