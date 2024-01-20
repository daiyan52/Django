from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def kol_jobs_views(request):
    s = '<h1>page for kolkata jobs</h1>'
    return HttpResponse(s)


def ptn_jobs_views(request):
    s = '<h1>page for patna jobs</h1>'
    return HttpResponse(s)


def hyd_jobs_views(request):
    s = '<h1>page for hydrabaad jobs</h1>'
    return HttpResponse(s)