from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    msg = '<p>i am from  first view</p>'
    return HttpResponse(msg)

def second(request):
    msg = '<p>i am from  second view</p>'
    return HttpResponse(msg)

def third(request):
    msg = '<p>i am from  third view</p>'
    return HttpResponse(msg)

def forth(request):
    msg = '<p>i am from  forth view</p>'
    return HttpResponse(msg)

def fifth(request):
    msg = '<p>i am from  fifth view</p>'
    return HttpResponse(msg)
