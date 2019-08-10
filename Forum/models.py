from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    user_type   = models.CharField(max_length=10)
    user_id     = models.IntegerField(default=0)
    title       = models.CharField(max_length=127)
    description = models.CharField(max_length=1024)
    created_at  = models.DateTimeField(auto_now_add=True)
    votes       = models.IntegerField(default=0)

class Comment(models.Model):
    user_type   = models.CharField(max_length=10)
    user_id     = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    votes       = models.IntegerField(default=0)
    post_id     = models.IntegerField(default=0)