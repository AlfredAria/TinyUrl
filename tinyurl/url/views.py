from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the url index.")

def write(request):
    return HttpResponse("Long to short request")

def lookup(request):
    return HttpResponse("Short to long request")