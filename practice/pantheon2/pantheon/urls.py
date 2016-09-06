"""pantheon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.get_countries_and_country_ids, name='countries'),
    url(r'^country/(?P<country_code>.+)/industry/(?P<industry>.+)/*', views.get_people_in_industry, name='people_in_industry'),
    url(r'^country/(?P<country_code>.+)$', views.get_country_code_to_industry, name='industries'),
    url(r'^persons/(?P<cur_id>.+)$', views.get_person_from_cur_id, name='people'),
]
