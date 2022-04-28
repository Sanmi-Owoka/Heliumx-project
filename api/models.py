from django.db import models
from authentication.models import User


class Newletter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Subscription(models.Model):
    TYPE = (
        ('basic', 'basic'),
        ('premium', 'premium')
    )
    type = models.CharField(max_length=255, choices=TYPE)
    details = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Session(models.Model):
    doctor_email = models.CharField(max_length=255)
    patient_email = models.CharField(max_length=255)
    meeting_link = models.CharField(max_length=255)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

