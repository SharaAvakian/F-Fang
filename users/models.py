from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# TODO: Extend User model with profile information (e.g., address, preferences)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields like phone, address, etc.
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
