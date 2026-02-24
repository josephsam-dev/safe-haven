from django.contrib import admin
from .models import CounselingSession
from notifications.models import Notification

@admin.register(CounselingSession)
class CounselingSessionAdmin(admin.ModelAdmin):
    list_display = ("user", "session_type", "scheduled_date", "status")
    list_editable = ("status",)

    def save_model(self, request, obj, form, change):
        if change:
            old = CounselingSession.objects.get(pk=obj.pk)
            if old.status != obj.status:
                Notification.objects.create(
                    user=obj.user,
                    message=f"Your counseling session on {obj.scheduled_date} is now {obj.get_status_display()}."
                )
        super().save_model(request, obj, form, change)
