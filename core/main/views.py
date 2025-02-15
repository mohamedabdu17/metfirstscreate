from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>Hello, world. You're at the main index.</h1>")

def about(response):
    return HttpResponse("<h1>About page</h1>")

def programs(response):
    return HttpResponse("<h1>Programs page</h1>")

def events(response):
    return HttpResponse("<h1>Events page</h1>")

def sponsor(response):
    return HttpResponse("<h1>Sponsor page</h1>")

