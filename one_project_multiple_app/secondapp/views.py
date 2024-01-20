from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def second_view(request):
    msg = '<h1>Hello i am second appp</h1>'
    return HttpResponse(msg)