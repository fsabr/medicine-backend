from django.db import models

# Create your models here.

class Doctor(models.Model):
    name     = models.CharField(max_length=255, blank=False, unique=False)
    email    = models.EmailField(max_length=255, blank=False, unique=True, null=False)
    password = models.CharField(max_length=255, blank=False, unique=False)

    def __str__(self):
        return self.email

class Patient(models.Model):
    name     = models.CharField(max_length=255, blank=False, unique=False)
    email    = models.EmailField(max_length=255, blank=False, unique=True, null=False)
    password = models.CharField(max_length=255, blank=False, unique=False)
    doctor   = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True)
    symptoms = models.CharField(max_length=1023, blank=False, null=True, unique=False)
    illness  = models.CharField(max_length=255, null=True, unique=False, blank=False)

    def __str__(self):
        return self.email

class Medicine(models.Model):
    IMAGE_PATH = 'images/'

    name  = models.CharField(max_length=255, blank=False, unique=False)
    image = models.ImageField(upload_to=IMAGE_PATH, max_length=1023)

    def __str__(self):
        return self.name