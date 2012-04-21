import uuid

def feed_id_processor(request):
    if request.user.is_authenticated():
        uf = UserFeed.objects.filter(user=request.user)
        if !uf.exists():
            uf = UserFeed(user=request.user, feed_id=uuid.uuid4().hex)
            uf.save()
        else:
            uf = uf[0]
        return {'feed_id': uf.feed_id}
    else:
        return {}
