from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Yeah, It is my first app and it is Working.")

# Create your views here.
