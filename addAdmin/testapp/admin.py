from django.contrib import admin
from testapp.models import Admin
# Register your models here.
class Admin_Admin(admin.ModelAdmin):
    list_display = ['name', 'dept',]
admin.site.register(Admin, Admin_Admin)