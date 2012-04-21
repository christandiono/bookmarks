from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Bookmark(models.Model):
    user = models.ForeignKey(User)
    status_id = models.IntegerField()
    comment_id = models.IntegerField()
