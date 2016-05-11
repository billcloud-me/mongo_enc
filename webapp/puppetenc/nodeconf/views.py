from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Welcome to the puppet configuration tool!")

# Create your views here.
