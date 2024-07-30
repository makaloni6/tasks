from django.contrib import admin
from .models import Task, TaskLog, MoodLog

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'estimated_time', 'slack_time', 'is_completed')
    list_filter = ('user', 'is_completed', 'due_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'due_date'

class TaskLogAdmin(admin.ModelAdmin):
    list_display = ('task', 'start_time', 'end_time', 'duration', 'is_slacking')
    list_filter = ('task__user', 'is_slacking', 'start_time')
    search_fields = ('task__title',)
    date_hierarchy = 'start_time'

class MoodLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'mood')
    list_filter = ('user', 'mood', 'date')
    date_hierarchy = 'date'

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskLog, TaskLogAdmin)
admin.site.register(MoodLog, MoodLogAdmin)