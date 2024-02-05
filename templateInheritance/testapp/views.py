from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request, 'html/Home.html')

def AboutView(request):
    return render(request, 'html/About.html')