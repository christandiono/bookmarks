from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Bookmark(models.Model):
    user = models.ForeignKey(User)
    fb_id = models.TextField() # ?!?!

    def get_url(self):
        return "https://facebook.com/posts/%s" % fb_id

    def __unicode__(self):
        return unicode(fb_id)

class UserFeed(models.Model): # authenticates a user to read a certain feed
    user = models.ForeignKey(User)
    feed_id = models.TextField(default=0)
