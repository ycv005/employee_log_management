from django.contrib import admin
from .models import Project, Activity, Entry


class EntryAdmin(admin.ModelAdmin):
    """
    Class to Showcase the Entry Admin
    """
    list_display = ('name', 'time_left',
                    'total_duration', 'user', 'project', 'activity')

    def time_left(self, obj):
        return obj.time_left

    def total_duration(self, obj):
        return obj.total_duration


class ActivityAdmin(admin.ModelAdmin):
    """
    Class to Showcase the Entry Admin
    """
    list_display = ('name', 'code')


admin.site.register(Project)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Entry, EntryAdmin)
