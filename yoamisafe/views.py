from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def map(request, username, longitude, latitude):
    return HttpResponse("Hello World")

def temp(request):
    return HttpResponse("Hello from temp")