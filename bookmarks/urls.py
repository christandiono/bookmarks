from django.conf.urls.defaults import patterns, include, url

import base

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookmarks.views.home', name='home'),
    # url(r'^bookmarks/', include('bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('bookmarks.facebook.auth.urls', namespace="facebook")),
    url(r'^$', base.views.index),
    url(r'^mine/$', base.views.my_bookmarks)
)
