from django.conf.urls import patterns, include, url
from apps.test_cup.views import *
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', ShowBio.as_view(), name='main'),
     url(r'^settings$',ShowSettings.as_view(), name='settings'),
     url(r'^last_10/$',ShowRequests.as_view(),name='requests'),
     url(r'^update_bio/(?P<pk>\d+)/$',
         login_required(UpdateBio.as_view()),name='update_bio'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
#    url(r'^accounts/profile/$',),
    # url(r'^cups/', include('cups.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))