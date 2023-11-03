# loginmodels.py

from django.db import models
from register.models import Registration

class UserProfile(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE,related_name='login_profile')
    # Additional fields specific to the UserProfile model
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Note: Use Django's built-in User model or another authentication system in a real-world application
