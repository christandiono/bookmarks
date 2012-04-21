from django.conf.urls.defaults import patterns, include, url


from bookmarks import base

from bookmarks.base.feeds import BookmarkFeed

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
    url(r'^$', 'bookmarks.base.views.index', name="index"),
    url(r'^mine/$', 'bookmarks.base.views.my_bookmarks', name="mine"),
    (r'^feed/(?P<user_id>\w+)/(?P<feed_id>[a-f0-9])/$', BookmarkFeed()),
    url(r'^api/submit/$','bookmarks.base.views.api_submit',name="submit")

)
