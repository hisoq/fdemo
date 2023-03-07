from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse

def index(request):
    return HttpResponse("phone")