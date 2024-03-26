from django.shortcuts import render
from testapp.models import Student
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    fields = '__all__'

class StudentUpdate(UpdateView):
    model = Student
    fields = ['roll','address']    

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('StudentList')