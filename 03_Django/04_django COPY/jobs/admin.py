from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin): 
    list_display = ('id', 'name', 'past_job',) #trailing comma 찍는 습관~
admin.site.register(Job, JobAdmin)
