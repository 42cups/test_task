from django.conf.urls import patterns, include, url
from apps.test_cup.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', ShowBio.as_view(), name='main'),
     url(r'^last_10/$', ShowRequests.as_view(), name='requests'),

    # url(r'^cups/', include('cups.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
