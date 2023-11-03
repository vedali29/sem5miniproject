# registrationmodels.py



from django.db import models

class Registration(models.Model):
    child_name = models.CharField(max_length=255)
    parent_name = models.CharField(max_length=255)
    relationship_to_child = models.CharField(max_length=255)
    child_birthdate = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
