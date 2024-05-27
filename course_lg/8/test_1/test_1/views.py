from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    a = 10
    return HttpResponse('index page')


