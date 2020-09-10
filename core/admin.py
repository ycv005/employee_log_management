from django.contrib import admin
from .models import Project, Activity, Entry
from django.utils import timezone


class ActiveFilter(admin.SimpleListFilter):
    title = parameter_name = 'active'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(end_time__gt=timezone.now())
        elif value == 'No':
            return queryset.exclude(end_time__gt=timezone.now())
        return queryset


class EntryAdmin(admin.ModelAdmin):
    """
    Class to Showcase the Entry Admin
    """
    list_display = ('name', 'total_duration',
                    'time_left', 'active', 'user', 'project',
                    'activity',
                    )

    list_filter = (ActiveFilter,)

    def time_left(self, obj):
        return obj.time_left

    def total_duration(self, obj):
        return obj.total_duration

    def active(self, obj):
        return obj.is_active

    active.boolean = True


class ActivityAdmin(admin.ModelAdmin):
    """
    Class to Showcase the Entry Admin
    """
    list_display = ('name', 'code')


admin.site.register(Project)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Entry, EntryAdmin)
