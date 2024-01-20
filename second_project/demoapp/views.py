from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def getTime(request):
    time = datetime.datetime.now()
    s = '<h2>Current time is: ' + str(time) + '</h2>'
    return HttpResponse(s)