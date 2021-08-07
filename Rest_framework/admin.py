from Rest_framework.models import Task
from django.contrib import admin

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','complete']
admin.site.register(Task, TaskAdmin)