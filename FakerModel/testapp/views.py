from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def StudentView(request):
    stu_list = Student.objects.all().order_by('-marks')
    my_dict = {'stu_list': stu_list}
    return render(request, 'HtmlFolder/index.html',my_dict)