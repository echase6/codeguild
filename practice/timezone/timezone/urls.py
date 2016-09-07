"""timezone URL Configuration."""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^time$', views.return_local_time,
        name='return_local_time'),
    url(r'^(?P<latlng>.+)/tz$', views.return_tz_at_latlng,
        name='return_tz_at_latlng'),
    url(r'^(?P<latlng>.+)/time$', views.return_time_at_latlng,
        name='return_time_at_latlng'),
    url(r'^(?P<in_time>.+)/at/(?P<latlng>.+)$',
        views.return_converted_time,
        name='return_converted_time')
]
