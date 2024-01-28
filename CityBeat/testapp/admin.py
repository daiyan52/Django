from django.contrib import admin
from testapp.models import Kolkata_job,Delhi_job,Bengaluru_job,Hyderabad_job
# Register your models here.
class Kolkata_job_Admin(admin.ModelAdmin):
    list_display = ('estd', 'company', 'position', 'eligibility', 'location', 'email', 'phone')
admin.site.register(Kolkata_job, Kolkata_job_Admin)

class Delhi_job_Admin(admin.ModelAdmin):
    list_display = ('estd', 'company', 'position', 'eligibility', 'location', 'email', 'phone')
admin.site.register(Delhi_job, Delhi_job_Admin)

class Bengaluru_job_Admin(admin.ModelAdmin):
    list_display = ('estd', 'company', 'position', 'eligibility', 'location', 'email', 'phone')
admin.site.register(Bengaluru_job, Bengaluru_job_Admin)

class Hyderabad_job_Admin(admin.ModelAdmin):
    list_display = ('estd', 'company', 'position', 'eligibility', 'location', 'email', 'phone')
admin.site.register(Hyderabad_job, Hyderabad_job_Admin)

