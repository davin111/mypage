from django.shortcuts import render


from django.http import HttpResponse

import datetime
from django.utils import timezone

def index(request):
    dt = timezone.localtime()
    now = dt.strftime("%Y.%m.%d. %H:%M:%S (%A)")
    return HttpResponse("Hello, world! Now is " + now + " (UTC) [posts]")
