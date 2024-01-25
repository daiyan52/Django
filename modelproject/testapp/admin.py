from django.contrib import admin
from testapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_no']

admin.site.register(Student, StudentAdmin)