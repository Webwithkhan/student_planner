from django.db import models
from django.conf import settings
from planner.models import Task

class Note(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="notes"
    )
    task = models.ForeignKey(
        Task, 
        on_delete=models.CASCADE, 
        related_name="notes", 
        null=True, 
        blank=True
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return f"{self.title} - {self.user.username}"
