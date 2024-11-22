from django.contrib import admin
from job.models import *
# Register your models here.
admin.site.register(Job)
admin.site.register(JobResponsibility)
admin.site.register(JobExperience)
admin.site.register(JobApplication)