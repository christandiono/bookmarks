# Create your views here.

from models import Bookmark

from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

@login_required
def my_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render_to_response('list.html', {'bookmarks': bookmarks}, context_instance=RequestContext(request))

