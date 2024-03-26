from django.contrib import admin
from testapp.models import Student
# Register your models here.
class StudentModel(admin.ModelAdmin):
    list_display = ('name', 'roll', 'address')
admin.site.register(Student, StudentModel)