from django.contrib import admin
from testapp.models import Student
# Register your models here.

class Student_admin(admin.ModelAdmin):
    list_display = ('name', 'roll','student_id', 'address')
admin.site.register(Student,Student_admin)