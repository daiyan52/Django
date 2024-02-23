from django.shortcuts import render
from .forms import videoDataForm
from .models import videoData
from django.http import HttpResponse
# Create your views here.

def videoView(request):
    if request.method == "POST":
        form = videoDataForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Successfully uploaded')
    else:
        form = videoDataForm()
    return render(request,'uploadVideo.html',{'form':form})
