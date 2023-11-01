from django.db import models

class UserProfile(models.Model):
    child_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


class Appointment(models.Model):
    child_name = models.CharField(max_length=255)
    email = models.EmailField()
    age_group = models.CharField(max_length=50)
    doctor = models.CharField(max_length=255)
    last_certificate = models.FileField(upload_to='certificates/')
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=20)
# Create your models here.
