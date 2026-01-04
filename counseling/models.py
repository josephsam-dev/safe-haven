from django.db import models
from django.contrib.auth.models import User

class CounselingSession(models.Model):
    SESSION_TYPE_CHOICES = [
        ('online', 'Online'),
        ('in_person', 'In Person'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_type = models.CharField(max_length=20, choices=SESSION_TYPE_CHOICES)
    message = models.TextField()
    scheduled_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.session_type}"
