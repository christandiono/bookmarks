# Create your views here.

from models import Bookmark
from models import UserFeed
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

@login_required
def my_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render_to_response('list.html', {'bookmarks': bookmarks}, context_instance=RequestContext(request))

def api_submit(request):
    if (request.method=='POST'):
        fbID=request.POST["fb_id"]
        UserFeed(fb_id=fbID, user=request.user).save()
        return HttpResponse("The reuqest is POST.")

