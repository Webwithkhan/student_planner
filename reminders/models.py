from django.db import models
from planner.models import Task
from django.conf import settings

class Reminder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='reminders', null=True, blank=True)
    message = models.CharField(max_length=255)
    remind_at = models.DateTimeField()

    def __str__(self):
        return f"Reminder for {self.task} at {self.remind_at}"
