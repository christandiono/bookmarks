from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
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
        return "%s %s" % (obj.user.first_name, obj.user.last_name)

    def link(self, obj):
        return 'http://electric-sword-7186.herokuapp.com%s' % reverse('mine')

    def description(self, obj):
        return "An RSS feed of your saved posts."

    def item_title(self, obj):
        return obj['data']['from']['name']

    def item_link(self, obj):
        return 'https://www.facebook.com/%s' % obj['id'].split('_')[0]

    def item_description(self, obj):
        return obj['message']

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

