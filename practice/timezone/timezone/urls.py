"""timezone URL Configuration."""

from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^time$', views.return_local_time),
    url(r'^(.+)/tz$', views.return_tz_at_latlng),
    url(r'^(.+)/time$', views.return_time_at_latlng),
    url(r'^(.+)/(.+)/as/(.+)$', views.return_converted_time)
]
