from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import CounselingSession
from notifications.models import Notification


@receiver(pre_save, sender=CounselingSession)
def create_notification_on_status_change(sender, instance, **kwargs):
    # New object → no notification yet
    if not instance.pk:
        return

    try:
        previous = CounselingSession.objects.get(pk=instance.pk)
    except CounselingSession.DoesNotExist:
        return

    # Only act if status changed
    if previous.status != instance.status:
        message = ""

        if instance.status == "confirmed":
            message = "Your counseling session has been confirmed."

        elif instance.status == "completed":
            message = "Your counseling session has been completed."

        elif instance.status == "pending":
            message = "Your counseling session is now pending."

        if message:
            Notification.objects.create(
                user=instance.user,
                message=message
            )
