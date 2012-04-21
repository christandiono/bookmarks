from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Bookmark(models.Model):
    user = models.ForeignKey(User)
    fb_id = models.TextField() # ?!?!

class UserFeed(models.Model): # authenticates a user to read a certain feed
    user = models.ForeignKey(User)
    feed_id = models.TextField()
