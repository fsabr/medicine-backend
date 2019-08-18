from django.db import models

# Create your models here.

class UploadedImage(models.Model):
    image = models.ImageField("Uploaded Image") # Store filename

class Base64(models.Model):
    image = models.CharField(max_length=104857600)