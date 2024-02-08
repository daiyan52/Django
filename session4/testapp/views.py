from django.shortcuts import render
from testapp.forms import *
# Create your views here.

def nameForm_View(request):
    form  = nameForm()
    return render(request,'pages/name.html',{'form':form})

def rollNumberForm_View(request):
    name = request.GET['name']
    request.session['name'] = name
    form  = rollNumberForm()
    return render(request,'pages/rollNumber.html',{'form':form,'name':name})

def deptForm_View(request):
    rollNumber = request.GET['rollNumber']
    request.session['rollNumber'] = rollNumber
    name = request.session['name']
    form  = deptForm()
    return render(request,'pages/dept.html',{'form':form,'name':name})

def result_View(request):
    dept = request.GET['dept']
    request.session['dept'] = dept
    return render(request,'pages/result.html')