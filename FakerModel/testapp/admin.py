from django.contrib import admin
from testapp.models import Student
# Register your models here.

class  StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_no','marks', 'dob', 'age', 'dept', 'email', 'phone', 'address']
admin.site.register(Student,StudentAdmin)