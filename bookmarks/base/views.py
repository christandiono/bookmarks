# Create your views here.

from models import Bookmark
from models import UserFeed
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

@login_required
def my_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user).order_by('-date')
    real_bookmarks = []
    bad = 0
    for mark in bookmarks:
        try:
            unicode(mark)
            if not mark.date:
                bad += 1
            else:
                real_bookmarks.append(mark)
        except:
            pass
    return render_to_response('list.html', {'bookmarks': real_bookmarks, 'bad': bad}, context_instance=RequestContext(request))

def api_submit(request):
    if (request.method=='POST'):
        fbID=request.POST["fb_id"]
        if not Bookmark.objects.filter(fb_id=fbID, user=request.user).exists():
            Bookmark(fb_id=fbID, user=request.user).save()
        return HttpResponse("The request is POST.")

