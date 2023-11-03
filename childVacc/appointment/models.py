# appointmentmodels.py


from django.db import models
from register.models import Registration

class Appointment(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='appointments')
    child_name = models.CharField(max_length=255)
    email = models.EmailField()
    age_group = models.CharField(max_length=50)
    doctor = models.CharField(max_length=255)
    last_vaccine_certificate = models.FileField(upload_to='vaccine_certificates/')
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=50)
    # Add other appointment fields if needed
