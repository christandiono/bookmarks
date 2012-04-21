from django.contrib.syndication.views import Feed
from bookmarks.base.models import Bookmark

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

import urllib2
import urllib

import dateutil

from models import UserFeed



class BookmarkFeed(Feed):

    def get_object(self, request, user_id, feed_id):
        return get_object_or_404(UserFeed, user__id=user_id, feed_id=feed_id)

    def title(self, obj):
        return obj.fb_id

    def link(self, obj):
        return obj.get_link()

    def description(self, obj):
        return obj.get_desc()

    def items(self, obj):
        marks = Bookmark.objects.filter(user=obj.user)
        all_comments = []
        for mark in marks:
            try:
                response = urllib2.urlopen('https://graph.facebook.com/%s?%s' % (obj.fb_id, urllib.urlencode(dict(access_token=user.password))))
                dumped = json.loads(response)
                comments = response.get('comments')
                if comments:
                    data = response.get('data')
                    for d in data:
                        all_comments.append(d)
            except:
                pass # ignore all problems
        my_cmp = lambda x, y: cmp(dateutil.parser.parse(x['created_time']), dateutil.parser.parse(y['created_time']))
        all_comments.sort(cmp=my_cmp)
        return all_comments

