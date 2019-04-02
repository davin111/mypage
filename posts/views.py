from django.shortcuts import render


from django.http import HttpResponse
from django.http import Http404

from .models import Post
from django.template import loader

from django.shortcuts import render, get_object_or_404

#import datetime
#from django.utils import timezone

def index(request):
    #dt = timezone.localtime()
    #now = dt.strftime("%Y.%m.%d. %H:%M:%S (%A)")

    latest_post_list = Post.objects.order_by('-pub_date')[:5] #show recent 5 posts, ordered by 'pub_date'
    context = {'latest_post_list': latest_post_list}

    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    return render(request, 'posts/detail.html', {'post': post})

def results(request, post_id):
    response = HttpResponse("You're looking at the results of post %s." % post_id)
    return HttpResponse(response)

def react(request, post_id):
    return HttpResponse("You're reacting on post %s." % post_id)