from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns('',
    url(r'^$', views.main_panel, name='main_panel'),
    url(r'^travel/', include('travel.urls', namespace='travel')),
)
