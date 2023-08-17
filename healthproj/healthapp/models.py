from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)


class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    email_id = models.CharField(max_length=100)
    place = models.CharField(max_length=500)

class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    email_id = models.CharField(max_length=100)
    designation = models.CharField(max_length=250)
    
