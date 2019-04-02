from django.shortcuts import render


from django.http import HttpResponse
from .models import Post

import datetime
from django.utils import timezone

def index(request):
    dt = timezone.localtime()
    now = dt.strftime("%Y.%m.%d. %H:%M:%S (%A)")

    latest_post_list = Post.objects.order_by('-pub_date')[:5] #show recent 5 posts, ordered by 'pub_date'
    output = ', '.join([p.content for p in latest_post_list])

    return HttpResponse("Hello, world! Now is " + now + " (Seoul) [posts]\n" + output)

def detail(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)

def results(request, post_id):
    response = HttpResponse("You're looking at the results of post %s." % post_id)
    return HttpResponse(response)

def react(request, post_id):
    return HttpResponse("You're reacting on post %s." % post_id)