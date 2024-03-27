from django.shortcuts import render
from testapp.models import Student,Teacher
# Create your views here.
def DataView(request):
    stu_list = Student.objects.all()
    tea_list = Teacher.objects.all()
    my_dict = {'stu_list': stu_list,'tea_list': tea_list}
    return render(request, 'index.html',my_dict)