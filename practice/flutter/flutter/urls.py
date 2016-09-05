"""flutter URL Configuration"""

from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.render_index, name="index"),
    url(r'^search$', views.render_query, name="query"),
    url(r'^post$', views.render_submit, name="submit"),
    url(r'^post/submit$', views.render_submit_ack, name="submit_ack")
]
