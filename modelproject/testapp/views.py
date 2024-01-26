from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def Student_View(request):
    stu_list = Student.objects.all()
    print(stu_list.count())
    my_dict = {'stu_list':stu_list}
    return render(request, 'HtmlFolder/index.html',context=my_dict)