from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.user_profile, name='profile'),
    url(r'^family/$', views.user_list, name='user_list'),
    url(r'^family/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
)

