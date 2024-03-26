from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
from django.db.models import Avg
# Create your views here.


def EmployeeView(request):
    # emp_list = Employee.objects.all()
    # emp_list = Employee.objects.filter(sal__gt=50000).order_by('sal')
    # emp_list = Employee.objects.filter(name__startswith='d')
    
    # OR
    
    #emp_list = Employee.objects.filter(name__startswith='S') | Employee.objects.filter(sal__lt=50000).order_by('sal')
    
    #emp_list = emp_list = Employee.objects.filter(Q(name__startswith='A') | Q(sal__gt=20000))

    # AND
    #emp_list = Employee.objects.filter(Q(name__startswith='A') & Q(sal__gt=20000)).order_by('sal')
    #emp_list = Employee.objects.filter(name__startswith='D', sal__gt=20000).order_by('sal')
    
    #emp_list = Employee.objects.filter(name__startswith='D', address__endswith='d')

    # NOT
    
    #emp_list = Employee.objects.filter(~Q(name__startswith='D')).order_by('name')
    
    emp_list = Employee.objects.all().order_by('name')
    
    sum = Employee.objects.all().aggregate(sum('sal'))
    avg = Employee.objects.all().aggregate(Avg('sal'))
    
    my_dict = {'emp_list': emp_list,'avg': avg,'sum': sum}
    return render(request, 'HtmlFolder/index.html',my_dict)