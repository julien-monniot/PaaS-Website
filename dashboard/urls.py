from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns('',
    url(r'^$', views.main_panel, name='main_panel'),
    url(r'^notifications/$', views.notifications, name='notifications'),
    url(r'^notifications/(?P<pk>\d+)/$', views.notification_link, name='notification_link'),
    )