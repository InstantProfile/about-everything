from django.contrib import admin
from .models import WorkEntry

@admin.register(WorkEntry)
class WorkEntryAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'hours_worked', 'date')
    search_fields = ('job_title', 'comment')
    list_filter = ('date',)
