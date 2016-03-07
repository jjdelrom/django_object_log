from django.contrib import admin
from object_log.models import LogAction, LogItem

class LogItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'action')
    list_filter = ('user', 'timestamp')


admin.site.register(LogAction)
admin.site.register(LogItem, LogItemAdmin)

