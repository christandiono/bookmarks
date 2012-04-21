from django.db import models

from django.contrib.auth.models import User

import json
import urllib2
import urllib

# Create your models here.


class Bookmark(models.Model):
    user = models.ForeignKey(User)
    fb_id = models.TextField() # ?!?!
    title = models.TextField(default="")
    description = models.TextField(default="")
    date=models.DateField(default=None)

    def get_url(self):
        return "https://www.facebook.com/%s" % self.fb_id

    def __unicode__(self):
        if not self.title and not self.description:
            try:
                response = urllib2.urlopen('https://graph.facebook.com/%s?%s' % (self.fb_id, urllib.urlencode(dict(access_token=self.user.password))))
                dumped = json.loads(response.read())
                self.title = dumped.get('from').get('name')
                self.description = dumped.get('message')
		if dumped.get('updated_time') or dumped.get('created_time'):
			timeConsist=dumped.get('updated_time').split('T')
			self.date=timeConsist[0]+" "+(timeConsist[1].split('+'))[0]
                self.save()
            except:
                pass # ignore all problems

        return unicode("%s--%s" % (self.title, self.description))

class UserFeed(models.Model): # authenticates a user to read a certain feed
    user = models.ForeignKey(User)
    feed_id = models.TextField(default=0)
