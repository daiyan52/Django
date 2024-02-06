from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request, 'testapp/home.html')

def languageView(request):
    return render(request, 'testapp/language.html')

def projectView(request):
    return render(request, 'testapp/project.html')

def contactView(request):
    return render(request, 'testapp/contact.html')