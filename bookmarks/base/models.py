from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Bookmark(models.Model):
    user = models.ForeignKey(User)
    fb_id = models.TextField() # ?!?!
    status_id = models.IntegerField()
    comment_id = models.IntegerField(blank=True, null=True)
    first_checked = models.DateField(auto_now_add=True)
    last_checked = models.DateField(auto_now=True)
    has_updates = models.BooleanField(default=False)

class UserFeed(models.Model): # authenticates a user to read a certain feed
    user = models.ForeignKey(User)
    fb_id = models.TextField()
