from django.contrib import admin

from histories.models import History


class HistoryAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin/histories.css',)
        }

    list_display = ('model_name', 'action_type', 'user', 'created_at',)
    readonly_fields = ('created_at',)

admin.site.register(History, HistoryAdmin)
