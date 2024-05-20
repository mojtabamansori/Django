from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("user settings")

def edit_profile(request):
    return HttpResponse("edit profile")

# Create your views here.
