from django.shortcuts import render
from testapp.models import Kolkata_job,Delhi_job,Bengaluru_job,Hyderabad_job
# Create your views here.
def Home_View(request):
    return render(request, 'HtmlFolder/home.html')
def Kolkata_View(request):
    job_list = Kolkata_job.objects.all()
    my_dict = {'job_list': job_list}
    return render(request, 'HtmlFolder/Kolkata_jobs.html',my_dict)