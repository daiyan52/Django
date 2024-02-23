from django.shortcuts import render,redirect
from testapp.models import Student
from testapp.forms import StudentForm

def insert_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    form = StudentForm()
    return render(request,'pages/insert.html',{'form':form})
def data_view(request):
    stu_list = Student.objects.all().order_by('name')
    return render(request, 'pages/data.html',{'stu_list':stu_list})

def delete_view(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')

def update_view(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'pages/update.html',{'form':form})