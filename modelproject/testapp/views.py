from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def Student_View(request):
    # stu_list = Student.objects.all()
    # stu_list = Student.objects.filter(name__startswith='A')
    # stu_list = Student.objects.filter(age__lt=25)
    # stu_list = Student.objects.all().order_by('age')
    stu_list = Student.objects.all().order_by('name')

    print(stu_list.count())
    my_dict = {'stu_list':stu_list}
    return render(request, 'HtmlFolder/index.html',context=my_dict)