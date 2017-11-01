from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserModel(models.Model):
    username=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)     
    phone=models.CharField(max_length=20)     
    email=models.CharField(max_length=20)     
    role=models.CharField(max_length=20)     
    status=models.CharField(max_length=20)
        
