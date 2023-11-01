from django.db import models

class UserProfile(models.Model):
    child_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

# Create your models here.
