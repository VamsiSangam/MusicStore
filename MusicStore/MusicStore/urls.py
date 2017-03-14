"""
Definition of urls for MusicStore.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^artists$', app.views.artists, name = 'artists'), # name is used in HTML page # {% url 'artists' %}
    url(r'^artists/(?P<id>\d+$)', app.views.artistdetails, name = 'artistdetails'),
    url(r'^artists/create$', app.views.create, name = 'createartist'),

    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^login/$', app.views.login, name = 'login'),
    url(r'^register/$', app.views.register, name = 'register'),
    url(r'^logout$', app.views.logout, name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
