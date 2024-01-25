from django.contrib import admin
from testapp.models import Stundent_Jis
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','marks']

admin.site.register(Stundent_Jis,StudentAdmin)