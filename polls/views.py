from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! Today is 2019.04.01.(Mon) [index]")
