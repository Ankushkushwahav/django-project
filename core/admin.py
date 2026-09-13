from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'completed',
        'created_at',
    )

    list_filter = (
        'completed',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
        'user__username',
    )

    ordering = (
        '-created_at',
    )


admin.site.site_header = 'Django Project Admin'
admin.site.site_title = 'Django Admin'
admin.site.index_title = 'Dashboard'
