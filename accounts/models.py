from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    university = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

