from django.contrib import admin
from testapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'sal', 'address')

admin.site.register(Employee, EmployeeAdmin)