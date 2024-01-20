from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
     msg = '<h1>Hello i am first appp</h1>'
     return HttpResponse(msg)
