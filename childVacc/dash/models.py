# dashboardmodels.py



from django.db import models
from django.contrib.auth.models import User
from register.models import Registration

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE,related_name='dashboard_profile')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    location = models.CharField(max_length=255, blank=True)
    # Add other profile fields if needed

