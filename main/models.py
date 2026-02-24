from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message[:30]}"

from django.db import models


class Donation(models.Model):

    name = models.CharField(max_length=150)

    email = models.EmailField()

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} - ₦{self.amount}"