from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sent = models.BooleanField(default=False)
